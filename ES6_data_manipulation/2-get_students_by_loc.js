/* eslint-disable */

const getStudentsByLocation = (studentsArray, city) => {
	return studentsArray.filter((student) => student.location === city);
}

export default getStudentsByLocation;