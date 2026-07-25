function copyToClipboard(event, text) {
    event.preventDefault();
    event.currentTarget.innerHTML = "<ins><i class=\"bi bi-check2\"></i><ins>";
    navigator.clipboard.writeText(text);
}

function downloadTextFile(event, title, contents) {
    event.preventDefault();
    event.currentTarget.innerHTML = "<ins><i class=\"bi bi-download\"></i><ins>";

    // 1. Create a modern content container (Blob) for plain text
    const blob = new Blob([contents], { type: 'text/plain;charset=utf-8' });

    // 2. Generate a secure, addressable URL pointing to the data
    const url = URL.createObjectURL(blob);

    // 3. Create a temporary, hidden link element
    const link = document.createElement('a');
    link.href = url;

    // 4. Enforce a download action and set the target file name
    link.download = title.endsWith('.txt') ? title : `${title}.txt`;

    // 5. Append the link to the DOM body to support older browsers
    document.body.appendChild(link);

    // 6. Programmatically fire the download prompt
    link.click();

    // 7. Housekeeping: Remove the link and free up system memory
    document.body.removeChild(link);
    URL.revokeObjectURL(url);
}