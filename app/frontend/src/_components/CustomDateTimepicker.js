import React, { useState } from "react";
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";
export const CustomDateTimepicker = (props) => {
  const [startDate, setStartDate] = useState(props.value);

  let handleColor = (time) => {
    return time.getHours() > 12 ? "text-success" : "text-error";
  };

  return (
    <DatePicker
      showTimeSelect
      selected={props.value}
      // onChange={(date) => setStartDate(date)}
      onChange={(date) => props.onChange(date)}
      timeClassName={handleColor}
    />
  );
};
