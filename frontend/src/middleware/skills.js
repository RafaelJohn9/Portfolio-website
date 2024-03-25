import axios from 'axios';

async function getSkills() {
    try {
        const response = await axios.get('http://localhost:5001/api/v1/skills');
        return response.data;
    } catch (error) {
        console.error(error);
    }
}

export default getSkills;