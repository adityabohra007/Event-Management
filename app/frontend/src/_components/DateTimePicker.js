import * as React from "react";
import TextField from "@mui/material/TextField";
import AdapterDateFns from "@mui/lab/AdapterDateFns";
import LocalizationProvider from "@mui/lab/LocalizationProvider";
import DateTimePicker from "@mui/lab/DateTimePicker";
import { ThemeProvider } from "@mui/system";
import { createTheme } from "@mui/material";
import { green, lime } from "@mui/material/colors";
export default function BasicDateTimePicker(props) {
  const [value, setValue] = React.useState(new Date());
  const defaultMaterialTheme = createTheme({
    palette: {
      primary: {
        light: "#757ce8",
        main: "#3f50b5",
        dark: "#002884",
        contrastText: "#fff",
      },
      secondary: {
        light: "#ff7961",
        main: "#f44336",
        dark: "#ba000d",
        contrastText: "#000",
      },
    },
  });
  return (
    <ThemeProvider theme={defaultMaterialTheme}>
      <LocalizationProvider dateAdapter={AdapterDateFns}>
        <DateTimePicker
          color={"primary"}
          renderInput={(props) => <TextField {...props} />}
          label={props.label}
          value={value}
          onChange={(newValue) => {
            setValue(newValue);
          }}
        />
      </LocalizationProvider>
    </ThemeProvider>
  );
}
