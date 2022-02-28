import React, { useEffect, useState } from "react";
import {
  StyledEventDetail,
  StyledPage,
  StyledSubTitle,
  StyledSubTitleDetail,
  StyledTitle,
} from "../_components/StyledPage";
import { eventService } from "../_services/event.service";
const UserEventDetailsPage = (props) => {
  const [event, setEvent] = useState(null);
  const [errorText, setErrorText] = useState(null);
  useEffect(async () => {
    var data = await eventService.getUserEventDetails(props.match.params.id);
    data = {
      ...data,
      booking_start: new Date(data.booking_start),
      booking_end: new Date(data.booking_end),
      scheduled_on: new Date(data.scheduled_on),
    };
    console.log(data);
    setEvent(data);
  }, []);

  const handleRegisterMe = async () => {
    try {
      const response = await eventService.postEventRegistration(
        props.match.params.id
      );
    } catch (e) {

        alert(e['non_field_error']);
      
    }
  };
  return (
    <StyledPage>
      {/* <CustomDateTimepicker></CustomDateTimepicker> */}
      {event ? (
        <StyledEventDetail>
          <div>
            <StyledTitle>{event.name}</StyledTitle>
            <div>
              <a onClick={() => handleRegisterMe()}>Register Me</a>
            </div>
          </div>
          <StyledSubTitle>Description</StyledSubTitle>
          <StyledSubTitleDetail>{event.description}</StyledSubTitleDetail>
          <div>
            <div>
              <StyledSubTitle>Timings</StyledSubTitle>
              <StyledSubTitleDetail>
                Booking start: <span>{event.booking_start.toDateString()}</span>
              </StyledSubTitleDetail>
              <StyledSubTitleDetail>
                Booking end: <span>{event.booking_end.toDateString()}</span>
              </StyledSubTitleDetail>
              <StyledSubTitleDetail>
                Show starts on: <span>{event.scheduled_on.toDateString()}</span>
              </StyledSubTitleDetail>
            </div>
            <div>
              <StyledSubTitle>Max Capacity</StyledSubTitle>
              <StyledSubTitleDetail>
                <span>{event.max_capacity}</span>
              </StyledSubTitleDetail>
            </div>
          </div>
        </StyledEventDetail>
      ) : (
        <p>Loading</p>
      )}
    </StyledPage>
  );
};

export default UserEventDetailsPage;
