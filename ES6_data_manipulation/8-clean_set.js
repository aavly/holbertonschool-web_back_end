/* eslint-disable */

const cleanSet = (set, startString) => {
	if (!startString || typeof startString !== 'string') return '';
  
	let result = '';
	const hyphen = '-';
  
	for (const string of set) {
	  if (string.startsWith(startString)) {
		const newString = string.slice(startString.length);
		if (result) {
		  result += hyphen; 
		}
		result += newString; 
	  }
	}
  
	return result;
  };
  
  export default cleanSet;