# Milestone 3 Project - Data Centric Development Milestone Project - Restaurant Booking System

<img width="1453" height="826" alt="am-i-responsive" src="https://github.com/user-attachments/assets/f673de24-b44c-431a-a633-aa8bacd21631" />

## Links

- [Link to Live Website](https://rpires71.github.io/milestone-3/)
- [GitHub Project Repository](https://github.com/rpires71/milestone-3)

## Table of contents

- [Milestone Project 3](README.md#milestone-project-3)
- [Portuguese Kitchen Booking System](README.md#portuguese-kitchen-booking-system)
  - [Project Overview](README.md#project-overview)
  - [Project Goals](README.md#project-goals)
  - [Purpose of the Website](README.md#purpose-of-the-website)
  - [Target Audiences](README.md#target-audiences)
  - [Key Features and Skills Demonstrated ](#key-features-and-skills-demonstrated)
  - [UX Strategy](#ux-strategy)
    - [Research and Planning](#research-and-planning)
    - [Design Principles](#design-principles)
    - [Testing and Feedback](#testing-and-feedback)
  - [Features](#features)
  - [Future Features](#future-features)
- [References](README-PT2.md#references)


# Milestone Project 3

Development Milestone Project 3 - Data Centric Development
[⬆ Back to Table of contents](#table-of-contents)

# Portuguese Kitchen Booking System

[⬆ Back to Table of contents](#table-of-contents)

## Project Overview

[⬆ Back to Table of contents](#table-of-contents)

The **Portuguese Kitchen Booking System** is a full-stack, database-driven web application developed as part of the **Back End Development – Milestone Project 3** for the **Level 5 Diploma in Web Application Development** (Code Institute, 2025). The project simulates a real-world restaurant booking system for a Portuguese-style restaurant, allowing users to **view availability, make table reservations, and manage bookings** through an intuitive online interface.

The application has been designed with a strong focus on **usability, accessibility, and responsive design**, ensuring a consistent and user-friendly experience across desktop, tablet, and mobile devices. **Semantic HTML**, a clear **visual hierarchy**, and logical navigation are used throughout to support a straightforward booking journey and to align with modern **user-centred design principles**.

From a technical perspective, the project uses **Python and a back-end web framework** to handle server-side logic, combined with **HTML5, CSS3, and template-based rendering** to dynamically display content. A **relational database** supports full **CRUD (Create, Read, Update, Delete)** functionality, enabling booking data to be securely stored, retrieved, updated, and removed as required. **Server-side validation** and **error handling** are implemented to maintain data integrity and provide clear feedback to users.

The project follows **professional development and deployment practices**, including the use of **environment variables** for sensitive configuration, dependency management via a `requirements.txt` file, and deployment to a **cloud-based hosting platform**. Comprehensive **manual testing** has been carried out to verify functionality, responsiveness, usability, and data handling, with findings documented as part of the project submission.

Overall, the Portuguese Kitchen Booking System demonstrates my ability to build a **publishable, real-world full-stack web application**, combining robust back-end development, database management, and user-focused design to deliver a practical and scalable restaurant booking solution.


## Project Goals

[⬆ Back to Table of contents](#table-of-contents)

The primary objective of the **Portuguese Kitchen Booking System** project is to design and develop a **user-centred, full-stack web application** that allows users to **view availability, make table reservations, and manage restaurant bookings** through a secure and intuitive online platform.

By incorporating **database-driven functionality**, **server-side logic**, **responsive interface design**, and **accessible navigation structures**, the project aims to fully satisfy the requirements outlined in the **Code Institute Back End Development – Milestone Project 3** specification (Code Institute, 2025).

### 1. Dynamic Full-Stack Functionality

The application provides full **CRUD (Create, Read, Update, Delete)** functionality, enabling users to create new bookings, view existing reservations, update booking details, and cancel reservations where applicable.

All server-side logic is handled using **Python and a back-end web framework**, with dynamic content rendered through **template-based views**. Booking data is securely stored and managed using a **relational database**, ensuring data persistence and integrity across user sessions.

### 2. Responsive and Accessible User Experience

The project is designed to deliver a **consistent and responsive user experience** across desktop, tablet, and mobile devices, ensuring accessibility and usability regardless of screen size or device type.

Accessibility considerations are incorporated in line with the **Web Accessibility Initiative (WAI)** guidelines, including clear navigation, readable typography, appropriate contrast, and meaningful form feedback to support inclusive user interaction (W3C, 2023).

### 3. User Interaction and Feedback

The system provides clear and immediate feedback to users during key interactions such as booking submissions, form validation, and error handling.

Server-side validation ensures that booking data is accurate and complete before being stored, while user-friendly messages guide users through the booking process and highlight any required corrections or confirmation of successful actions.

### 4. Information Architecture and Navigation

A **logical information architecture** is implemented through a clear page hierarchy and consistent navigation structure, ensuring that users can easily move between pages such as viewing availability, making reservations, and managing bookings.

The use of **semantic HTML** enhances accessibility, maintainability, and search engine optimisation (SEO), while supporting best practices in modern web application development (Mozilla Developer Network, 2024).


### 5. Secure Data Handling and Configuration

Sensitive configuration data, including secret keys and environment-specific settings, are managed using **environment variables** to ensure security and flexibility across development and deployment environments.

The application incorporates appropriate **error handling and data validation** mechanisms to protect user data and maintain system stability.

### 6. Version Control and Deployment

Throughout the development lifecycle, **Git and GitHub** are used to manage version control, track changes, and document development progress in a transparent and professional manner.

The final version of the application is deployed to a **cloud-based hosting platform**, ensuring public accessibility and demonstrating an understanding of modern deployment workflows for full-stack applications (Code Institute, 2025).

### 7. Documentation and Attribution

Comprehensive project documentation is provided within the `README.md` file, outlining the project’s purpose, features, technologies used, and deployment details.

All external resources, libraries, and references are clearly credited in accordance with **Code Institute’s attribution and academic integrity guidelines** (Code Institute, 2025).

---

### Outcome

By achieving these objectives, the **Portuguese Kitchen Booking System** demonstrates a strong level of proficiency in **back-end web application development**, including the effective use of **server-side logic**, **database-driven functionality**, and **template-based rendering** to deliver a fully operational booking platform.

In line with the standards expected at **Level 5 Web Application Development**, the completed project showcases both **technical competence** and **professional presentation**, reflecting a clear understanding of **user-focused design**, **secure data handling**, and **real-world application development practices** (Code Institute, 2025).

## Purpose of the Website

[⬆ Back to Table of contents](#table-of-contents)

I have developed the **Portuguese Kitchen Booking System**, which forms a core component of the **Level 5 Diploma in Web Application Development** and constitutes my **Full Stack Web Application Development – Milestone Project 3**.

This project demonstrates the practical application of **server-side development**, **database-driven functionality**, and **user-centred design**, resulting in a fully functional restaurant booking platform. The system enables users to explore the restaurant, view key information, and make table reservations through an intuitive and structured web interface.

Designed to reflect a real-world restaurant environment, the booking system allows users to submit reservation requests that are securely processed and stored within a relational database. Administrators are able to manage bookings and content through a protected administration interface, ensuring efficient control over restaurant operations.

The application has been developed using **Django**, **Python**, **HTML**, **CSS**, **JavaScript**, and **PostgreSQL**, incorporating **template-based rendering**, **CRUD functionality**, and **form validation** to ensure data integrity and a reliable user experience. Responsive design principles and **semantic HTML** are applied throughout to guarantee accessibility and usability across multiple devices.

From a development perspective, the project adheres to professional full stack development standards by implementing **secure authentication**, **environment-based configuration**, and **structured application architecture**. Version control is maintained using **Git and GitHub**, and the final application is deployed to **Heroku**, ensuring public accessibility and compliance with modern deployment practices.

The completed **Portuguese Kitchen Booking System** is a polished and accessible web application that demonstrates the ability to translate real-world business requirements into a secure, database-backed solution, reflecting both **technical competence** and **professional presentation** in line with current industry expectations.

## Target Audiences

[⬆ Back to Table of contents](#table-of-contents)

By utilising this interactive and informative platform, several interconnected user groups with a shared interest in dining experiences and restaurant bookings will recognise that the **Portuguese Kitchen Booking System** has been specifically developed to meet their needs. Each audience benefits from tailored functionality and a user experience that prioritises **accessibility**, **clarity**, and **operational efficiency** (W3C, 2023; Interaction Design Foundation, 2023).

## 1. Restaurant Customers and Diners

The booking system enables customers to explore the restaurant offering, view essential information, and reserve tables through a simple and intuitive interface. This makes the platform particularly suitable for individuals or couples seeking a reliable and convenient way to plan dining experiences in advance.

Users are supported in making informed booking decisions through clear presentation of availability, structured reservation forms, and confirmation feedback, ensuring a smooth and frustration-free user journey.

## 2. Families and Group Bookings

The system is designed to accommodate families and larger groups by allowing flexible reservation requests while maintaining clarity and ease of use. Responsive design ensures that bookings can be made seamlessly across mobile devices, tablets, and desktop systems, supporting users who may plan meals collaboratively or on the move.

By streamlining the booking process, the platform reduces friction and enhances confidence when organising group dining arrangements.

## 3. Restaurant Owners and Administrators

For restaurant staff and administrators, the booking system provides a secure and centralised environment for managing reservations and customer data. Through the protected admin interface, authorised users can view, update, and manage bookings efficiently, supporting daily restaurant operations and capacity planning.

This functionality reflects real-world restaurant management workflows and highlights the system’s practical business value.

## 4. Hospitality Professionals and Educational Reviewers

The project demonstrates effective implementation of **full stack web development principles**, including database integration, secure authentication, and server-side processing. As such, it serves as a valuable reference for hospitality professionals, assessors, and educational reviewers seeking insight into modern, user-centred booking systems.

The application showcases how **technical functionality**, **accessibility considerations**, and **professional presentation** can be combined to deliver a robust, real-world web solution (Code Institute, 2025).

---

Supported by contemporary web technologies and user-centred design principles, the **Portuguese Kitchen Booking System** delivers a clear, accessible, and intuitive booking experience. Whether browsing restaurant information or reserving a table, the system ensures that the needs of all user groups are effectively supported through consistent design, responsive layout, and straightforward interaction flows.

## Key Features and Skills Demonstrated

[⬆ Back to Table of contents](#table-of-contents)

The development of this interactive, user-focused full-stack web application, **Portuguese Kitchen Booking System**, demonstrates a strong level of technical competence and professional design practice. Modern web technologies, server-side development principles, and accessibility standards have been applied to deliver a secure, reliable, and user-friendly restaurant booking platform.

- **Database-Driven Functionality and Server-Side Processing**

To support real-world booking operations, the application implements a **relational database** to store and manage reservation data, enabling full **CRUD (Create, Read, Update, Delete)** functionality. Server-side logic is handled using **Python and the Django web framework**, allowing booking availability, form submissions, and data validation to be processed securely and efficiently (Code Institute, 2025).

- **Responsive and Accessible Interface Design**

To ensure consistent usability across desktop, tablet, and mobile devices, **responsive web design techniques** incorporating **CSS Grid**, **Flexbox**, and **media queries** were applied (Mozilla Developer Network, 2024). Accessibility considerations were implemented in line with the **Web Accessibility Initiative (WAI)** guidelines published by the **World Wide Web Consortium (W3C, 2023)**, using semantic HTML, clear navigation structures, and meaningful visual hierarchy.

- **Dynamic User Interaction and Validation**

Dynamic behaviour within the application is achieved through a combination of **template-based rendering**, **server-side validation**, and **JavaScript-enhanced interactivity**. Users receive clear feedback during booking submissions, error handling, and confirmation stages, ensuring a transparent and user-friendly reservation process (Mozilla Developer Network, 2024).

- **User-Centred Design and Visual Consistency**

The interface has been designed with a strong emphasis on **user-centred design principles**, prioritising clarity, ease of navigation, and accessibility. Consistent typography, colour hierarchy, and layout structure contribute to a visually coherent experience that supports efficient task completion and reduces user friction (Interaction Design Foundation, 2023).

- **Secure Configuration and Deployment Practices**

Sensitive configuration data, including secret keys and environment-specific settings, are managed using **environment variables**, ensuring secure separation between development and production environments. The completed application is deployed to a **cloud-based hosting platform**, demonstrating compliance with modern full-stack deployment workflows (Code Institute, 2025).

- **Version Control and Development Workflow**

**Git and GitHub** were utilised throughout the development lifecycle to manage version control, track progress, and maintain a transparent development history. This approach supports iterative development and reflects professional software engineering practices (Code Institute, 2025).

- **Professional Documentation and Code Quality**

A comprehensive `README.md` file documents the project’s purpose, features, technologies used, testing processes, and deployment steps. The codebase follows modular, maintainable conventions and includes appropriate in-line comments, ensuring readability and long-term maintainability in line with professional development standards (Code Institute, 2025).

---

This project demonstrates the successful integration of **user-centred design**, **responsive interface development**, and **database-driven server-side functionality** to deliver a fully operational restaurant booking system. The final outcome reflects both **technical competence** and **professional presentation**, meeting the standards expected at **Level 5 Web Application Development**.

## UX Strategy

[⬆ Back to Table of contents](#table-of-contents)

The UX strategy for the **Portuguese Kitchen Booking System** is structured around a **user-centred design approach**, ensuring that the application meets the practical needs of both customers and administrators while remaining accessible, intuitive, and efficient (Interaction Design Foundation, 2023).

The strategy is divided into three key phases:

- Research and Planning  
- Design Principles  
- Testing and Feedback

Throughout development, the UX strategy prioritises **accessibility**, **clarity**, **responsiveness**, **data accuracy**, and **ease of interaction**, in line with **Web Accessibility Initiative (WAI)** guidelines and modern usability standards (W3C, 2023).

### Research and Planning

[⬆ Back to Table of contents](#table-of-contents)

This phase focuses on identifying and understanding the primary user groups for the booking system, including:

- Restaurant customers and diners  
- Families and group diners  
- Restaurant administrators and staff  

User needs, expectations, and goals are explored through the creation of **user personas** and **usage scenarios**, reflecting real-world restaurant booking behaviours such as selecting a date and time, submitting reservation details, and receiving booking confirmation (Nielsen Norman Group, 2022).

Key research considerations include:

- How users expect to book tables online  
- What information users require before confirming a reservation  
- How administrators manage bookings efficiently  

Features and content are prioritised based on relevance to each user group, ensuring that booking forms, availability information, and confirmation feedback are clearly presented and easy to understand (Code Institute, 2025).

### Design Principles

[⬆ Back to Table of contents](#table-of-contents)

- **Accessibility:**  
  Semantic HTML5 and a logical heading structure are used throughout the application. Form fields include clear labels and validation messages to support screen reader users. Colour contrast and readable typography are applied to ensure inclusive access, particularly for booking forms and confirmation alerts (W3C, 2023).

- **Responsiveness:**  
  A mobile-first approach is implemented using **CSS Grid**, **Flexbox**, and **media queries** to ensure consistent usability across desktop, tablet, and mobile devices (Mozilla Developer Network, 2024). Booking forms and navigation elements adapt seamlessly to different screen sizes.

- **Navigation:**  
  Clear and consistent navigation allows users to move intuitively between viewing restaurant information, checking availability, making reservations, and managing bookings. The booking journey is designed to minimise steps and reduce friction (Interaction Design Foundation, 2023).

- **Visual Hierarchy:**  
  Typography, spacing, and layout consistency are used to guide user attention towards key actions such as submitting a booking or reviewing reservation details. White space is applied strategically to reduce cognitive load and improve readability (Mozilla Developer Network, 2024).

- **Interactivity:**  
  Interactive elements such as booking forms, confirmation messages, and admin management views provide immediate and meaningful feedback. Clear calls to action guide users through the reservation process from start to completion.

- **Performance:**  
  Efficient server-side processing and optimised database queries ensure fast response times when submitting or retrieving booking data. Pages are structured to load efficiently without unnecessary delays.

- **Error Handling:**  
  Comprehensive server-side validation ensures that incomplete or invalid booking data is handled gracefully. User-friendly error messages clearly explain required corrections, while confirmation messages reinforce successful actions (Mozilla Developer Network, 2024).

### Testing and Feedback

[⬆ Back to Table of contents](#table-of-contents)

Manual usability testing is conducted across **desktop**, **tablet**, and **mobile** devices to ensure consistent behaviour and responsiveness. Particular emphasis is placed on the booking workflow, form interaction, and administrative booking management.

The following testing strategies are applied:

- **Form validation testing** for missing or invalid input  
- **CRUD functionality testing** for creating, viewing, updating, and deleting bookings  
- **Cross-browser testing** using Chrome, Firefox, and Edge (Mozilla Developer Network, 2024)  
- **HTML and CSS validation** using W3C validation tools (W3C, 2023)  

Performance and accessibility are evaluated using **browser developer tools** and **Google Lighthouse**, focusing on load efficiency, accessibility scores, and usability metrics. Keyboard-only navigation and screen reader compatibility are also tested to support users with disabilities (WebAIM, 2023).

Feedback gathered during testing is used to refine user flow, improve clarity, and enhance overall usability, particularly within the reservation journey.

---

This UX strategy ensures that the **Portuguese Kitchen Booking System** delivers a **clear**, **accessible**, and **professionally structured user experience**, reflecting best practices in **data-centric full-stack web development** and aligning with the expectations of **Milestone Project 3**.

## Features

[⬆ Back to Table of contents](#table-of-contents)

The **Portuguese Kitchen Booking System** is a full-stack, database-driven web application developed to simulate a real-world restaurant reservation platform. A key feature of the system is its ability to allow users to **view restaurant information, check table availability, and submit booking requests** through a structured and interactive web interface that reflects contemporary web application standards (Code Institute, 2025).

Rather than relying on third-party travel or mapping APIs, the system focuses on **server-side logic and database integration** to manage booking data securely and efficiently. All reservation details, including **date selection**, **guest numbers**, and **contact information**, are processed through validated forms and stored within a **relational PostgreSQL database**, ensuring data persistence and integrity. Logical defaults, such as preventing bookings for past dates and enforcing sensible guest limits, are implemented to support accurate and user-friendly submissions.

The booking workflow provides users with clear feedback at every stage of interaction. **Server-side validation** ensures that incomplete or invalid submissions are identified before processing, while **confirmation and error messages** guide users through the reservation process in a clear and accessible manner. This structured approach enhances usability and reduces the likelihood of booking errors, contributing to a smooth and reliable user experience.

From a design perspective, the application follows a **mobile-first, responsive layout**, utilising **CSS Grid**, **Flexbox**, and media queries to ensure consistent display and usability across desktop, tablet, and mobile devices (Mozilla Developer Network, 2024). The interface maintains a clean and professional aesthetic, with consistent typography, spacing, and visual hierarchy guiding users naturally through the booking journey.

Interactive enhancements such as **hover effects**, **form feedback states**, and **progressive content loading** are incorporated to improve engagement without compromising performance. Error handling is implemented gracefully, providing informative alerts when required fields are missing or when invalid input is detected, ensuring users are supported throughout their interaction with the system.

Overall, the **Portuguese Kitchen Booking System** delivers a refined, accessible, and user-centred reservation experience. By combining **robust back-end development**, **secure data handling**, and **responsive front-end design**, the project demonstrates the practical application of full-stack development principles and reflects the standards expected at **Level 5 Web Application Development**.

---

## Future Features

[⬆ Back to Table of contents](#table-of-contents)

As part of the planned future development of the **Portuguese Kitchen Booking System**, several enhancements have been identified to further improve usability, personalisation, and operational efficiency within a secure, data-driven environment.

Registered users will be able to **save favourite reservations**, **store preferred booking details**, and **track past and upcoming bookings** through a secure authentication system. These features aim to support repeat customers by streamlining the booking process and enhancing user engagement. A planned **customer feedback and review system** will allow diners to leave ratings and comments following their visit, providing valuable insights for both prospective customers and restaurant administrators.

To improve reservation accuracy and flexibility, enhanced filtering options are planned, including **party size selection**, **time-slot availability**, **seating preferences**, and **special dietary requirements**. These filters will enable users to tailor bookings more precisely while allowing administrators to manage capacity and table allocation more effectively.

To support informed booking decisions, future iterations of the system will integrate **external APIs** to provide contextual information such as **local weather forecasts** for dining dates (OpenWeather, 2024). This feature is particularly useful for outdoor seating considerations. Additionally, a **booking management dashboard** will allow users to organise multiple reservations, modify existing bookings, and plan dining schedules in advance.

For transparency and operational insight, a **pricing and availability comparison view** is planned, enabling administrators to analyse peak times, booking trends, and demand patterns. Integration with additional third-party services may be introduced to support promotional offers or special events (Booking.com, 2024; Expedia Group, 2024).

Social engagement will be enhanced through **social sharing functionality**, allowing users to share confirmed reservations or restaurant experiences via social media platforms. This feature supports organic promotion while improving customer engagement (Meta for Developers, 2024; X Developers, 2024).

Accessibility remains a key priority for future development. Planned enhancements include expanded **ARIA labelling**, improved **keyboard navigation**, and optional **high-contrast display modes** to ensure full compliance with **Web Accessibility Initiative (WAI)** guidelines (W3C, 2023).

To accommodate a diverse user base, **automatic language detection** based on browser settings will support multilingual content delivery. Performance optimisations such as **lazy loading of assets**, improved database query efficiency, and caching strategies will be implemented to ensure reliable performance, even on slower network connections (Mozilla Developer Network, 2024).

Finally, the system is intended to evolve into a **Progressive Web App (PWA)**, enabling users to install the application on their devices and access selected features offline. This enhancement will improve accessibility, performance, and overall user experience while aligning the project with modern full-stack web application standards (Google Developers, 2024).

---


## References

[⬆ Back to Table of contents](#table-of-contents)

- **Code Institute (2025).** Data Centric Development – Milestone Project 3 Specification.
Dublin: Code Institute. Available at: https://learn.codeinstitute.net
  (Accessed: 27 December 2025).

- **W3C – World Wide Web Consortium (2023).** Web Content Accessibility Guidelines (WCAG) 2.2.
Available at: https://www.w3.org/WAI/standards-guidelines/wcag/
  (Accessed: 27 December 2025).

- **Mozilla Developer Network (MDN) (2024).** HTML, CSS and Web Development Documentation.
Available at: https://developer.mozilla.org/
  (Accessed: 27 December 2025).

- **Mozilla Developer Network (MDN) (2024).** Responsive Web Design and Front-End Development Documentation.
Available at: https://developer.mozilla.org/
  (Accessed: 27 December 2025).

- **Mozilla Developer Network (2024).** CSS Layout: Flexbox and Grid.  
Available at: https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout  
  (Accessed: 27 December 2025).

- **Mozilla Developer Network (2024).** Form Validation.  
Available at: https://developer.mozilla.org/en-US/docs/Learn/Forms/Form_validation  
  (Accessed: 27 December 2025).

- **Mozilla Developer Network (MDN) (2024).** CSS Grid Layout.
Available at: https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_grid_layout
  (Accessed: 27 December 2025).

- **Mozilla Developer Network (MDN) (2024).** HTML: Semantic elements.
Available at: https://developer.mozilla.org/en-US/docs/Glossary/Semantics
  (Accessed: 27 December 2025).

- **Mozilla Developer Network (2024).** Web Performance Optimisation and Lazy Loading.
Available at: https://developer.mozilla.org/en-US/docs/Web/Performance  
  (Accessed: 27 December 2025).

- **Interaction Design Foundation (2023).** User-Centred Design and Usability Principles.
Available at: https://www.interaction-design.org/
 (Accessed: 27 December 2025).

- **Nielsen Norman Group (2022).** User Personas and Scenario-Based Design. 
Available at: https://www.nngroup.com/articles/personas-scenarios/  
  (Accessed: 27 December 2025).

- **Web Accessibility Initiative (WAI), W3C (2023).** Web Content Accessibility Guidelines (WCAG) 2.2. 
Available at: https://www.w3.org/WAI/standards-guidelines/wcag/  
  (Accessed: 27 December 2025).

- **Booking.com (2024).** Partner Solutions and Booking Platform Overview.
Available at: https://partner.booking.com/  
  (Accessed: 27 December 2025).

- **Expedia Group (2024).** Expedia Group Developer Platform. 
Available at: https://developers.expediagroup.com/  
  (Accessed: 27 December 2025).

- **Google Developers (2024).** Progressive Web Apps (PWA) Documentation. 
Available at: https://developer.chrome.com/docs/webapps/  
  (Accessed: 27 December 2025).

- **Meta for Developers (2024).** Sharing Content on Facebook and Instagram. 
Available at: https://developers.facebook.com/docs/sharing/  
  (Accessed: 27 December 2025).

- **OpenWeather (2024).** OpenWeather API Documentation.
Available at: https://openweathermap.org/api  
  (Accessed: 27 December 2025).

- **X Developers (2024).** _X (formerly Twitter) Platform Developer Documentation._  
Available at: https://developer.x.com/  
  (Accessed: 27 December 2025).

