import React, { useEffect, useState } from "react";
import { eventService } from "../_services/event.service";
import { FaImage } from "react-icons/fa";
import "./index.css";

const AdminPage = () => {
  const [events, setEvents] = useState([]);
  useEffect(async () => {
    const data = await eventService.getEvents();
    console.log(data);
    setEvents(data);
  }, []);
  return (
    <div className="PageWrapper">
      <div className="allEvent">
        <div className="title">All Events by you</div>
        <div style={{ padding: "20px 40px", display: "flex" }}>
          {events.length ? (
            events.map((item) => (
              <a href={"/event/" + item.id} className="cardWrapper">
                <div className="cardImageWrapper">
                  <FaImage color={"gray"} size={"50%"}></FaImage>
                </div>
                <div className="cardInfoWrapper">
                  <div className="title">{item.name}</div>
                  <div className="description">{item.description}</div>
                </div>
              </a>
            ))
          ) : (
            <h1>No Events</h1>
          )}
        </div>
      </div>
    </div>
  );
};

export { AdminPage };
