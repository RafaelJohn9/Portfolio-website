async function getMusicUrl(music_query) {
    const url = 'https://www.johnmkagunda.me/api/v1/user/music/download';

    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ query: music_query })
        });

        if (response.ok) {
            const data = await response.json();
            const { url } = data;

            if (isValidUrl(url)) {
                return url;
            }
        }

        return null;
    } catch (error) {
        console.error('Error:', error);
        return null;
    }
}

function isValidUrl(url) {
    try {
        new URL(url);
        return true;
    } catch (error) {
        return false;
    }
}

async function downloadMusic(url) {
    try {
        const response = await fetch(url);
        if (response.ok) {
            const blob = await response.blob();
            const downloadUrl = URL.createObjectURL(blob);
            const link = document.createElement('a');
            link.href = downloadUrl;
            link.download = 'music.mp3';
            link.click();
        } else {
            return null;
        }
    } catch (error) {
        console.error('Error:', error);
        return null;
    }
}

export { getMusicUrl, downloadMusic }