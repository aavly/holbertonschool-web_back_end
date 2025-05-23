/* eslint-disable */

const updateStudentGradeByCity = (studentsList, city, newGrades=[]) => {
	return studentsList
		.filter((student) => student.location === city)
		.map((student) => {
			const gradeObject = newGrades.find((grade) => grade.studentId === student.id);
			return {
			  ...student,
			  grade: gradeObject ? gradeObject.grade : "N/A",
			};
		  });
};
export default updateStudentGradeByCity;