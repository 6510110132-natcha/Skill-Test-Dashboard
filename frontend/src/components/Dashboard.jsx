import { useEffect, useState } from 'react';
import axios from 'axios';

export default function Dashboard() {
  const [employees, setEmployees] = useState([]);

  useEffect(() => {
    axios.get('https://skill-test-dashboard-1.onrender.com/employees')
      .then(res => setEmployees(res.data));
  }, []);

  return (
    <table className="min-w-full border border-gray-300">
      <thead>
        <tr className="bg-gray-100">
          <th className="p-2 border">Employee Name</th>
          <th className="p-2 border">Join Date</th>
          <th className="p-2 border">Role</th>
          <th className="p-2 border">Team Member</th>
        </tr>
      </thead>
      <tbody>
        {employees.map((emp, idx) => (
          <tr key={idx} className="hover:bg-gray-50">
            <td className="p-2 border">{emp.name}</td>
            <td className="p-2 border">{emp.join_date}</td>
            <td className="p-2 border">{emp.role}</td>
            <td className="p-2 border">{emp.team_member}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}