/**
 * 
 * @returns the music file download
 */
const downloadMusic = async (query) => {
    try {
        const response = await fetch('https://www.johnmkagunda.me/api/v1/user/music/download', {
            method: 'POST',
            headers: {
            'Content-Type': 'application/json',
            },
            body: JSON.stringify({ query: query }),
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const blob = await response.blob();
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.style.display = 'none';
        a.href = url;
        a.download = query + '.mp3'; // you can set the filename here
        document.body.appendChild(a);
        a.click();
        window.URL.revokeObjectURL(url);
        } catch (error) {
        console.error('Error downloading the file:', error);
        }
  };
export { downloadMusic };