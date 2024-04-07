import axios from 'axios';

// axios.defaults.withCredentials = true

async function postItem(item) {
    const baseUrl = 'https://www.johnmkagunda/api/v1/user/';
    const { item_type: itemType } = item;
    let route;

    switch (itemType) {
        case 'music':
            route = 'music/recommend';
            break;
        case 'movie':
            route = 'movie/recommend';
            break;
        case 'books':
            route = 'books/recommend';
            break;
        default:
            return { status: 400, message: 'Invalid item type' };
    }

    try {
        const response = await axios.post(`${baseUrl}${route}`, item);
        return { ...response.data };
    } catch (error) {
        return { status: 500, message: 'Server error' };
    }
}

export default postItem;
