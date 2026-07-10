import json
import re
import urllib.request


def download_gw1_skill_dictionary():
    print("Fetching full skill database from Guild Wars Wiki...")
    url = "https://wiki.guildwars.com/wiki/Skill_template_format/Skill_list"

    try:
        # Request the official wiki page
        req = urllib.request.Request(
            url, headers={"User-Agent": "GW1-Template-Decoder-Parser"}
        )
        with urllib.request.urlopen(req) as response:
            html = response.read().decode("utf-8")

        print("Parsing skills...")
        pattern = re.compile(r'<tr>\s*<td>(\d+)</td>\s*<td>(?:<a[^>]*>)?([^<]+)')
        matches = pattern.findall(html)

        # Build the dictionary (mapping string/int ID to Name)
        skill_dict = {int(skill_id): name.strip()  for skill_id, name in matches}
        return skill_dict

    except Exception as e:
        print(f"Error downloading skill database: {e}")
        return None


if __name__ == "__main__":
    skills = download_gw1_skill_dictionary()

    with open("skills.py", "w", encoding="utf-8") as file:
        file.write("SKILLS = {\n")

        for id in skills:
            file.write(f"    {id}: {json.dumps(skills[id])},\n")

        file.write("}\n")
    
    print("Done!")