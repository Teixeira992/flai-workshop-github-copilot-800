import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import './App.css';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';

function App() {
  return (
    <div className="App">
      <nav className="navbar navbar-expand-lg navbar-dark bg-primary">
        <div className="container-fluid">
          <Link className="navbar-brand" to="/">OctoFit Tracker</Link>
          <button 
            className="navbar-toggler" 
            type="button" 
            data-bs-toggle="collapse" 
            data-bs-target="#navbarNav" 
            aria-controls="navbarNav" 
            aria-expanded="false" 
            aria-label="Toggle navigation"
          >
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav">
              <li className="nav-item">
                <Link className="nav-link" to="/users">Users</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/teams">Teams</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/activities">Activities</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/workouts">Workouts</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/leaderboard">Leaderboard</Link>
              </li>
            </ul>
          </div>
        </div>
      </nav>

      <div className="container-fluid px-4">
        <Routes>
          <Route path="/" element={
            <div className="container mt-4">
              <div className="hero-section">
                <h1>🏋️ Welcome to OctoFit Tracker</h1>
                <p className="lead">Track your fitness journey, compete with your team, and achieve your goals!</p>
              </div>
              
              <div className="row mb-4">
                <div className="col-md-3 mb-3">
                  <div className="stats-card">
                    <h3>👥</h3>
                    <p>Users</p>
                    <Link to="/users" className="btn btn-primary btn-sm mt-2">View All</Link>
                  </div>
                </div>
                <div className="col-md-3 mb-3">
                  <div className="stats-card">
                    <h3>🏆</h3>
                    <p>Teams</p>
                    <Link to="/teams" className="btn btn-primary btn-sm mt-2">View All</Link>
                  </div>
                </div>
                <div className="col-md-3 mb-3">
                  <div className="stats-card">
                    <h3>🏃</h3>
                    <p>Activities</p>
                    <Link to="/activities" className="btn btn-primary btn-sm mt-2">View All</Link>
                  </div>
                </div>
                <div className="col-md-3 mb-3">
                  <div className="stats-card">
                    <h3>💪</h3>
                    <p>Workouts</p>
                    <Link to="/workouts" className="btn btn-primary btn-sm mt-2">View All</Link>
                  </div>
                </div>
              </div>

              <div className="row">
                <div className="col-md-12">
                  <div className="card">
                    <div className="card-body text-center">
                      <h3 className="mb-3">🎯 Quick Actions</h3>
                      <Link to="/leaderboard" className="btn btn-success btn-lg me-2 mb-2">
                        View Leaderboard
                      </Link>
                      <Link to="/activities" className="btn btn-info btn-lg me-2 mb-2">
                        Log Activity
                      </Link>
                      <Link to="/workouts" className="btn btn-warning btn-lg mb-2">
                        Browse Workouts
                      </Link>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          } />
          <Route path="/users" element={<Users />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/activities" element={<Activities />} />
          <Route path="/workouts" element={<Workouts />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
        </Routes>
      </div>
    </div>
  );
}

export default App;
