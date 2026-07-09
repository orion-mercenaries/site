function copyToClipboard(event, text) {
    event.preventDefault();
    event.currentTarget.innerHTML = "<i class=\"bi bi-check2\"></i>";
    navigator.clipboard.writeText(text);
}