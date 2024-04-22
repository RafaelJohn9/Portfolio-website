async function postCommand(command) {
    const url = 'https://www.johnmkagunda.me/api/v1/projects/shell';
    const data = {
        command: command
    };

    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    });

    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    }

    const result = await response.json();
    return result;
}

postCommand('ls')
    .then(data => console.log(data))
    .catch(error => console.log('There was an error!', error));