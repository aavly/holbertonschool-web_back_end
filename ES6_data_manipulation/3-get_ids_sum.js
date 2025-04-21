/* eslint-disable */

const getStudentIdsSum = (studentsList) => {
	return studentsList.reduce((sum, student) => {
		return sum + student.id;
	}, 0);
}

export default getStudentIdsSum;