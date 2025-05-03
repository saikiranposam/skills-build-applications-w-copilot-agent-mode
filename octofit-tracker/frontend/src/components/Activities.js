import React, { useEffect, useState } from 'react';

function Activities() {
  const [activities, setActivities] = useState([]);

  useEffect(() => {
    fetch('https://symmetrical-space-parakeet-65vw5rpwpwc5jj5-8000.app.github.dev/api/activities/')
      .then(res => res.json())
      .then(data => setActivities(data));
  }, []);

  return (
    <div className="card mb-4">
      <div className="card-header bg-primary text-white"><h2 className="h4">Activities</h2></div>
      <div className="card-body">
        <table className="table table-striped">
          <thead>
            <tr>
              <th>User</th>
              <th>Type</th>
              <th>Distance</th>
              <th>Reps</th>
              <th>Points</th>
            </tr>
          </thead>
          <tbody>
            {activities.map((activity, idx) => (
              <tr key={idx}>
                <td>{activity.user}</td>
                <td>{activity.type}</td>
                <td>{activity.distance || '-'}</td>
                <td>{activity.reps || '-'}</td>
                <td>{activity.points}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Activities;
