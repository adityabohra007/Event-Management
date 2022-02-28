import React, { useEffect, useState } from "react";
import { eventService } from "../_services/event.service";
import { FaImage } from "react-icons/fa";
// import "./index.css";
import {
  EventCard,
  StyledPage,
  StyledSection,
  StyledTitle,
} from "../_components/StyledPage";

const UserEventPage = () => {
  const [events, setEvents] = useState([]);
  useEffect(async () => {
    const data = await eventService.getUserEvents();
    console.log(data);
    setEvents(data);
  }, []);
  return (
    <StyledPage>
      <StyledSection>
        <StyledTitle> Events </StyledTitle>
        <div style={{ display: "flex", flexWrap: "wrap" }}>
          {events.map((item) => (
            <EventCard
              redirect_to={"/user/event/" + item.id}
              item={item}
            ></EventCard>
          ))}
        </div>
      </StyledSection>
    </StyledPage>
  );
};

export { UserEventPage };
