export default function createEmployeesObject(departmentName, employees) {
  const employeeList = employees;

  return { [departmentName]: employeeList };
}
