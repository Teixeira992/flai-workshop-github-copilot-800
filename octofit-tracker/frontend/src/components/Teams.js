import React, { useState, useEffect } from 'react';

const Teams = () => {
  const [teams, setTeams] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchTeams = async () => {
      try {
        const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/teams/`;
        console.log('Fetching teams from:', apiUrl);
        
        const response = await fetch(apiUrl);
        
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        console.log('Teams data received:', data);
        
        // Handle both paginated (.results) and plain array responses
        const teamsData = data.results || data;
        console.log('Teams array:', teamsData);
        
        setTeams(teamsData);
        setLoading(false);
      } catch (err) {
        console.error('Error fetching teams:', err);
        setError(err.message);
        setLoading(false);
      }
    };

    fetchTeams();
  }, []);

  if (loading) {
    return (
      <div className="container mt-4 text-center">
        <div className="spinner-border spinner-border-custom text-primary" role="status">
          <span className="visually-hidden">Loading...</span>
        </div>
        <p className="mt-3">Loading teams...</p>
      </div>
    );
  }
  
  if (error) {
    return (
      <div className="container mt-4">
        <div className="alert alert-danger" role="alert">
          <h4 className="alert-heading">Error!</h4>
          <p>{error}</p>
        </div>
      </div>
    );
  }

  return (
    <div className="container mt-4">
      <div className="card">
        <div className="card-header">
          <h2 className="mb-0">🏆 Teams</h2>
        </div>
        <div className="card-body">
          {teams.length === 0 ? (
            <div className="alert alert-info" role="alert">
              No teams found. Create a team and start competing!
            </div>
          ) : (
            <>
              <div className="mb-3">
                <span className="badge bg-primary">Total Teams: {teams.length}</span>
              </div>
              <div className="table-responsive">
                <table className="table table-striped table-hover">
                  <thead>
                    <tr>
                      <th>ID</th>
                      <th>Team Name</th>
                      <th>Description</th>
                      <th>Created Date</th>
                    </tr>
                  </thead>
                  <tbody>
                    {teams.map((team) => (
                      <tr key={team.id}>
                        <td><span className="badge bg-secondary">{team.id}</span></td>
                        <td><strong>{team.name}</strong></td>
                        <td>{team.description}</td>
                        <td>{new Date(team.created_at).toLocaleDateString()}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </>
          )}
        </div>
      </div>
    </div>
  );
};

export default Teams;
