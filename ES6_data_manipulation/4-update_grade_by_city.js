/* eslint-disable */

const updateStudentGradeByCity = (studentsList, city, newGrades="N/A") => {
	return studentsList
		.filter(student => student.location === city)
		.map(student => ({
			...student,
			grade: newGrades,
		}));
};

export default updateStudentGradeByCity;