import React from "react";
import { FaImage } from "react-icons/fa";

import styled from "styled-components";
import { colors } from "../styles/colors";
export const StyledPage = styled.div`
  height: 500px;
  width: 100%;
`;

export const StyledSection = styled.div`
  width: 80%;
  margin: auto;
  padding: 20px 20px;
  background: white;
  margin-top: 30px;
`;
export const StyledEventDetail = styled.div`
  width: 80%;
  margin: auto;
  padding: 20px 20px;
  background: white;
  margin-top: 30px;
`;

export const StyledTitle = styled.div`
  margin: 0px;
  font-size: 18px;
  font-weight: 600;
  color: black;
`;

export const StyledSubTitle = styled.div`
  margin: 0px;
  font-size: 16px;
  color: black;
  font-weight: 600;
  margin-top: 20px;
`;

export const StyledSubTitleDetail = styled.div`
  padding: 20px 40px;
  display: flex;
  color: black;
`;

export const StyledEventEdit = styled.div`
  width: 80%;
  margin: auto;
  padding: 20px 20px;
  background: white;
  margin-top: 30px;
`;

export const StyledInput = styled.input`
  outline: none;
  max-width: 400px;
  border: 2px solid transparent;
  background: #eeeeee;
  &:focus {
    border: 2px solid ${colors.darkBlue && colors.darkBlue};
  }
`;

export const StyledInputWrapper = styled.div`
  display: flex;
  flex-direction: column;
  label: {
    font-size: 14px;
  }
`;

export const StyledButton = styled.button`
  margin-top: 10px;
  padding: 15px 10px;
  background-color: ${colors.darkBlue && colors.darkBlue};
  border: 0px;
  width: 100%;
  text-align: center;
  max-width: 400px;
  border-radius: 10px;
  color: ${colors.light};
  font-weight: 600;
  font-size: 16px;
`;

export const StyledEventCard = styled.a`
  background: white;
  border-radius: 2px;
  width: 200px;
  min-width: 200px;
  margin: 20px;
  display: flex;
  flex-direction: column;
  text-decoration: none;
  .cardImageWrapper {
    display: flex;
    justify-content: center;
    align-items: center;
    color: white;
    background: ${colors.blue && colors.blue};
    .imageLogo {
      color: white;
    }
  }

  .cardInfoWrapper {
    background: ${colors.light && colors.extraLight};
    padding: 10px;
    height: 100%;
    max-height: 100px;
    text-overflow: hidden;
  }
  .cardInfoWrapper .title {
    font-size: 18px;
    font-weight: 600;
    color: #151d3b;
  }
  .cardInfoWrapper .description {
    font-size: 18px;
    margin-top: 20px;
    font-weight: 200;
    text-overflow: ellipsis;
    max-height: min-content;
    overflow: hidden;
    white-space: nowrap;
    color: #151d3b;
  }
`;

export const EventCard = (props) => {
  return (
    <StyledEventCard href={props.redirect_to} className="cardWrapper">
      <div className="cardImageWrapper">
        <FaImage className="imageLogo" size={"50%"}></FaImage>
      </div>
      <div className="cardInfoWrapper">
        <div className="title">{props.item.name}</div>
        <div className="description">{props.item.description}</div>
      </div>
    </StyledEventCard>
  );
};
