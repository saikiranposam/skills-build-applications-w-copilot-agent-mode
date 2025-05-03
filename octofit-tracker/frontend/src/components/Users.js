import React, { useEffect, useState } from 'react';

function Users() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetch('https://symmetrical-space-parakeet-65vw5rpwpwc5jj5-8000.app.github.dev/api/users/')
      .then(res => res.json())
      .then(data => setUsers(data));
  }, []);

  return (
    <div className="card mb-4">
      <div className="card-header bg-primary text-white"><h2 className="h4">Users</h2></div>
      <div className="card-body">
        <table className="table table-striped">
          <thead>
            <tr>
              <th>Name</th>
              <th>Email</th>
              <th>Team</th>
            </tr>
          </thead>
          <tbody>
            {users.map((user, idx) => (
              <tr key={idx}>
                <td>{user.name}</td>
                <td>{user.email}</td>
                <td>{user.team}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Users;
