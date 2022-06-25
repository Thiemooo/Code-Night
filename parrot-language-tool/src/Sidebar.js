import './Sidebar.css';

function Sidebar() {
  
    return (
      <div className="sidebar">
        <button>Lückensatztraining</button>
        <button>Vokabeltrainer</button>
        <button href="./Donation.js" target = "_blank">Donate here!</button>
      </div>
    );
  }
  
  export default Sidebar;