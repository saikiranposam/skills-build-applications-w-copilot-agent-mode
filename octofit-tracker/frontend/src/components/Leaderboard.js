import React, { useEffect, useState } from 'react';

function Leaderboard() {
  const [leaderboard, setLeaderboard] = useState([]);

  useEffect(() => {
    fetch('https://symmetrical-space-parakeet-65vw5rpwpwc5jj5-8000.app.github.dev/api/leaderboard/')
      .then(res => res.json())
      .then(data => setLeaderboard(data));
  }, []);

  return (
    <div>
      <h2>Leaderboard</h2>
      <ul>
        {leaderboard.map((entry, idx) => (
          <li key={idx}>{entry.team} - {entry.points} points</li>
        ))}
      </ul>
    </div>
  );
}

export default Leaderboard;
