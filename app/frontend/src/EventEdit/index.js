import React, { useEffect, useState } from "react";
import { CustomDateTimepicker } from "../_components/CustomDateTimepicker";
import { eventService } from "../_services/event.service";
import {
  StyledButton,
  StyledEventEdit,
  StyledInput,
  StyledInputWrapper,
  StyledPage,
  StyledTitle,
} from "./../_components/StyledPage";

export const EventEdit = (props) => {
  const [event, setEvent] = useState(null);
  const [errorText, setErrorText] = useState(null);
  useEffect(async () => {
    var data = await eventService.getEventDetails(props.match.params.id);
    data = {
      ...data,
      booking_start: new Date(data.booking_start),
      booking_end: new Date(data.booking_end),
      scheduled_on: new Date(data.scheduled_on),
    };
    console.log(data);
    setEvent(data);
  }, []);

  const handleSubmit = async (e) => {
    console.log(props.history);
    e.preventDefault();
    try {
      const response = await eventService.postEventEdit(
        props.match.params.id,
        event
      );
      window.location = "/event/" + props.match.params.id;
    } catch (e) {
      setErrorText(e);
    }
  };
  const handleChange = (e) => {
    e.preventDefault();
    const { name, value } = e.target;
    setEvent({ ...event, [name]: value });
  };
  const handleChangeBookingStart = (date) => {
    console.log("dateee", date);
    setEvent({ ...event, booking_start: date });
  };
  const handleChangeBookingEnd = (date) => {
    setEvent({ ...event, booking_end: date });
  };
  const handleChangeScheduledOn = (date) => {
    setEvent({ ...event, scheduled_on: date });
  };
  return (
    <StyledPage>
      <StyledEventEdit>
        <StyledTitle>Edit a event</StyledTitle>
        <div style={{ padding: "5px 10px", color: "red" }}>
          {errorText &&
            errorText.non_field_errors &&
            errorText.non_field_errors[0]}
        </div>
        {event ? (
          <form onSubmit={handleSubmit} style={{ padding: 10 }}>
            <StyledInputWrapper>
              <label>Name</label>
              <StyledInput
                onChange={handleChange}
                placeholder="Enter Name"
                type={"text"}
                name={"name"}
                value={event.name}
              ></StyledInput>
              <div>{errorText && errorText.name && errorText.name[0]}</div>
            </StyledInputWrapper>
            <StyledInputWrapper>
              <label>Description</label>
              <StyledInput
                name="description"
                onChange={handleChange}
                value={event.description}
                placeholder="Enter Description"
                type={"text"}
              ></StyledInput>
              {errorText && errorText.description && errorText.description[0]}
            </StyledInputWrapper>
            <StyledInputWrapper>
              <label>Booking Starts</label>
              <CustomDateTimepicker
                name={"booking_start"}
                onChange={(date) => {
                  console.log("start", date);
                  handleChangeBookingStart(date);
                }}
                value={event.booking_start}
              ></CustomDateTimepicker>
              {errorText &&
                errorText.booking_start &&
                errorText.booking_start[0]}
            </StyledInputWrapper>
            <StyledInputWrapper>
              <label>Booking Ends</label>
              <CustomDateTimepicker
                name={"booking_start"}
                onChange={(date) => {
                  console.log("start", date);
                  handleChangeBookingEnd(date);
                }}
                value={event.booking_end}
              ></CustomDateTimepicker>
              {errorText && errorText.booking_end && errorText.booking_end[0]}
            </StyledInputWrapper>
            <StyledInputWrapper>
              <label>Scheduled</label>
              <CustomDateTimepicker
                onChange={(date) => {
                  console.log("start", date);
                  handleChangeScheduledOn(date);
                }}
                value={event.scheduled_on}
              ></CustomDateTimepicker>
              {errorText && errorText.scheduled_on && errorText.scheduled_on[0]}
            </StyledInputWrapper>
            <StyledInputWrapper>
              <label>Max Capacity</label>
              <StyledInput
                name="max_capacity"
                onChange={handleChange}
                value={event.max_capacity}
                placeholder="Enter Max Capacity"
                type={"number"}
              ></StyledInput>
              {errorText && errorText.max_capacity && errorText.max_capacity[0]}
            </StyledInputWrapper>
            <StyledButton>Submit</StyledButton>
          </form>
        ) : (
          <></>
        )}
      </StyledEventEdit>
    </StyledPage>
  );
};
