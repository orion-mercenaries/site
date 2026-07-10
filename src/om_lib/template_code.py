from markupsafe import Markup

# Mapping tables based on the official Guild Wars 1 Wiki specification
PROFESSIONS = [
    "None",
    "Warrior",
    "Ranger",
    "Monk",
    "Necromancer",
    "Mesmer",
    "Elementalist",
    "Assassin",
    "Ritualist",
    "Paragon",
    "Dervish",
]

ATTRIBUTES = {
    0: "Fast Casting",
    1: "Illusion Magic",
    2: "Domination Magic",
    3: "Inspiration Magic",
    4: "Blood Magic",
    5: "Death Magic",
    6: "Soul Reaping",
    7: "Curses",
    8: "Air Magic",
    9: "Earth Magic",
    10: "Fire Magic",
    11: "Water Magic",
    12: "Energy Storage",
    13: "Healing Prayers",
    14: "Smiting Prayers",
    15: "Protective Prayers",
    16: "Divine Favor",
    17: "Strength",
    18: "Axe Mastery",
    19: "Hammer Mastery",
    20: "Swordsmanship",
    21: "Tactics",
    22: "Beast Mastery",
    23: "Expertise",
    24: "Marksmanship",
    25: "Wilderness Survival",
    29: "Scythe Mastery",
    30: "Wind Prayers",
    31: "Earth Prayers",
    32: "Communing",
    33: "Restoration Magic",
    34: "Channeling Magic",
    35: "Critical Strikes",
    36: "Spawning Power",
    37: "Spear Mastery",
    38: "Command",
    39: "Motivation",
    40: "Leadership",
    44: "Mysticism",
}


class GuildWarsBitReader:
    """Decodes GW1 template strings character-by-character into a strict 6-bit stream."""

    def __init__(self, b64_str):
        # Standard Base64 alphabet used by Guild Wars
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
        char_map = {char: idx for idx, char in enumerate(alphabet)}

        self.bits = []
        # Clean string of any whitespace or padding characters
        clean_str = b64_str.strip().rstrip("=")

        for char in clean_str:
            if char in char_map:
                val = char_map[char]
                # GW1 reads each 6-bit character from LSB to MSB
                for b in range(6):
                    self.bits.append((val >> b) & 1)
        self.pos = 0

    def read(self, num_bits):
        if self.pos + num_bits > len(self.bits):
            return 0

        bit_segment = self.bits[self.pos : self.pos + num_bits]
        self.pos += num_bits

        # Reconstruct the integer value (lowest bit first)
        val = 0
        for i, bit in enumerate(bit_segment):
            if bit:
                val |= 1 << i
        return val


def decode_gw1_template(template_code, title):
    try:
        reader = GuildWarsBitReader(template_code)

        # 1. Header (Template Type & Version)
        # We peek ahead to see if it's a post-2007 template (starts with Type 14)
        # or an legacy template (starts directly with Version 0)
        first_4_bits = reader.read(4)

        if first_4_bits == 14:
            # Post-April 2007 format: Type (14) followed by Version (4 bits)
            template_type = "Skill Template"
            version = reader.read(4)
        elif first_4_bits == 15:
            # Equipment template (Type 15)
            return {
                "error": "This is an Equipment Template. Only Skill templates are supported."
            }
        else:
            # Legacy format pre-2007: The first 4 bits *are* the version number (usually 0)
            template_type = "Legacy Skill Template"
            version = first_4_bits

        # 2. Professions
        prof_bit_code = reader.read(2)
        bits_per_profession_id = prof_bit_code * 2 + 4

        primary_id = reader.read(bits_per_profession_id)
        secondary_id = reader.read(bits_per_profession_id)

        primary_prof = (
            PROFESSIONS[primary_id]
            if primary_id < len(PROFESSIONS)
            else f"Unknown ({primary_id})"
        )
        secondary_prof = (
            PROFESSIONS[secondary_id]
            if secondary_id < len(PROFESSIONS)
            else f"Unknown ({secondary_id})"
        )

        # 3. Attributes
        num_attributes = reader.read(4)
        attr_bit_code = reader.read(4)
        bits_per_attribute_id = attr_bit_code + 4

        attributes = {}
        for _ in range(num_attributes):
            attr_id = reader.read(bits_per_attribute_id)
            attr_value = reader.read(4)
            attr_name = ATTRIBUTES.get(attr_id, f"Unknown Attribute ({attr_id})")
            attributes[attr_name] = attr_value

        # 4. Skills
        skill_bit_code = reader.read(4)
        bits_per_skill_id = skill_bit_code + 8

        skill_ids = []
        for _ in range(8):
            skill_id = reader.read(bits_per_skill_id)
            skill_ids.append(skill_id)

        return {
            "title": title,
            "template_code": template_code,
            "template_type": template_type,
            "version": version,
            "primary_profession": primary_prof,
            "secondary_profession": secondary_prof,
            "attributes": attributes,
            "skill_ids": skill_ids,
        }

    except Exception as e:
        return {
            "error": f"Failed to decode template due to unexpected structure: {str(e)}"
        }
