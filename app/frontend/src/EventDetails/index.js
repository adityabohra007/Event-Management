import React, { useEffect, useState } from "react";
import {
  StyledEventDetail,
  StyledPage,
  StyledSubTitle,
  StyledSubTitleDetail,
  StyledTitle,
} from "../_components/StyledPage";
import { eventService } from "../_services/event.service";
const EventDetails = (props) => {
  //   const { id } = useParams();
  const [event, setEvent] = useState(null);
  const [booking, setBooking] = useState(null);

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
    var res = await eventService.getEventBookings(props.match.params.id);
    setBooking(res);
  }, []);
  return (
    <StyledPage>
      {/* <CustomDateTimepicker></CustomDateTimepicker> */}
      {event ? (
        <StyledEventDetail>
          <div>
            <StyledTitle>{event.name}</StyledTitle>
            <div>
              <a href={"/event/" + props.match.params.id + "/edit"}>Edit</a>
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
          <StyledSubTitle>Bookings</StyledSubTitle>
          <div style={{ padding: 20 }}>
            {booking ? (
              booking.map((item, index) => (
                <div style={{ display: "flex" }}>
                  <div>{index + 1}</div>
                  <div style={{ marginLeft: 10 }}>
                    {" "}
                    {item.user.user.username.toUpperCase()}
                  </div>
                </div>
              ))
            ) : (
              <></>
            )}
          </div>
        </StyledEventDetail>
      ) : (
        <p>Loading</p>
      )}
    </StyledPage>
  );
};

export default EventDetails;
