/**
 * File Name: processQueryParam.js
 * Description: This file contains the JavaScript code to process the query
 *  parameters. It removes the name attribute for empty inputs. This is done
 * to prevent empty inputs from being included in the query parameters.
 * Author: MathTeixeira
 * Date: July 6, 2024
 * Version: 4.0.0
 * License: MIT License
 * Contact Information: mathteixeira55
 */
document.getElementById("searchForm").onsubmit = function () {
  var elements = this.elements;
  for (var i = 0; i < elements.length; i++) {
    if (elements[i].type === "text" && elements[i].value === "") {
      elements[i].name = ""; // Temporarily remove name attribute for empty inputs
    }
  }
};
