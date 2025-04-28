/* eslint-disable */

const getFullResponseFromAPI = (success) => {
	return new Promise((resolve, reject) => {
		if (success) {
			const object = { status: 200, body: 'Success' };
			resolve(object);
		} else { 
			throw "The fake API is not working currently";
		}
	});
}


export default getFullResponseFromAPI;