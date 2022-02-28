import React, { useEffect, useState } from "react";
import {
  StyledPage,
  StyledSection,
  StyledTitle,
} from "../_components/StyledPage";
import { eventService } from "../_services/event.service";

export const MyBookings = () => {
  const [events, setEvents] = useState([]);
  useEffect(async () => {
    const res = await eventService.getUserBookings();
    setEvents(res);
  }, []);
  return (
    <StyledPage>
      <StyledSection>
        <StyledTitle>My Bookings</StyledTitle>
        <div>
          {events.map((item, index) => (
            <div style={{marginBotton:10}}>
              <div>{index + 1}</div>
              <div>{item.event.name}</div>
              <div>{item.event.description}</div>
            </div>
          ))}
        </div>
      </StyledSection>
    </StyledPage>
  );
};
