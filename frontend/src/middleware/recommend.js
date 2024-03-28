import axios from 'axios';

async function recommend(item) {
    let url = '';
    const baseUrl = 'http://localhost:5000/api/v1/user';

    switch(item.item_type) {
        case 'music':
            url = `${baseUrl}/music/recommend`;
            break;
        case 'book':
            url = `${baseUrl}/book/recommend`;
            break;
        case 'movie':
            url = `${baseUrl}/movie/recommend`;
            break;
        default:
            throw new Error('Invalid item_type');
    }

    try {
        const response = await axios.post(url, item);
        return response;
    } catch (error) {
        console.error(error);
    }
}

export default recommend;