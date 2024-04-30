/**
 * used to fetch response from my created shell
 */
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
    if (result['$'].includes('\r')) {
        result['$'] = result['$'].replace(/\r/g, ' ');
    }
    console.log(result);
    return result['$'];
}

export default postCommand;