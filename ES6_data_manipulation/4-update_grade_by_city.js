/* eslint-disable */

const updateStudentGradeByCity = (studentsList, city, newGrades="N/A") => {
	const filterStudents = studentsList.filter((student) => student.location == city);
	
	return filterStudents.map((student) => {
		return {...student, grade: newGrades};
	});
};

export default updateStudentGradeByCity;
