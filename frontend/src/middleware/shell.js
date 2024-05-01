/**
 * used to fetch response from my created shell
 */
const responseFormatter = (response) =>{
    if(response){
        response['$'] = response['$'].replace(/\n(?!\r$)/g, '\n\r');
        response['$'] = response['$'].replace(/\r$/, ''); // Remove \r from the end of the string
    }
    return response;
}

async function postCommand(command) {
    const url = 'https://www.johnmkagunda.me/api/v1/projects/shell';
    const data = {
        command: command.replace(/"/g, "'")
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

    let result = await response.json();
    result = responseFormatter(result);
    // if (result['$'].includes('\r')) {
    //     result['$'] = result['$'].replace(/\r/g, ' ');
    // }

    console.log(result);
    return result['$'];
}

export default postCommand;