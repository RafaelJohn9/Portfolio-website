import axios from 'axios';

async function getSkills() {
    try {
        const instance = axios.create({
            baseURL: 'http://localhost:5001/api/v1'
        });
        const response = await instance.get('/skills');
        const data = response.data;
        for (let key in data) {
            if (data[key].images) {
            for (let imgKey in data[key].images) {
                let base64Image = data[key].images[imgKey];
                // decode base64 image
                let decodedImage = atob(base64Image);
                // save decoded image back to the same key
                data[key].images[imgKey] = decodedImage;
            }
            }
        }
        return data;
    } catch (error) {
        console.error(error);
    }
}

export default getSkills;