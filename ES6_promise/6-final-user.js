/* eslint-disable */

import signUpUser from './4-user-promise.js';
import uploadPhoto from './5-photo-reject.js';

export default function handleProfileSignup(firstName, lastName, fileName) {
	return Promise.allSettled([
		signUpUser(firstName, lastName),
		uploadPhoto(fileName),
	]).then(
		(results) => results.map(
			(result) => {
				const newResult = {
			  		status: result.status,
				};
	
		if (result.status === 'rejected') {
			newResult.value = result.reason.toString();
		} else {
			newResult.value = result.value;
		}
			return newResult;
		  },
		),
	  );
	}