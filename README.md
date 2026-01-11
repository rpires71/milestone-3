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
  - [Technologies Used](#technologies-used)
  - [Wireframes](#wireframes)
  - [Portuguese Kitchen Booking System Wireframes](#portuguese-kitchen-booking-system-wireframes)
  - [User Story 1: View Available Time Slots (Customer)](#user-story-1-view-available-time-slots-customer)
  - [User Story 2: Specify the Number of Guests (Customer)](#user-story-2-specify-the-number-of-guests-customer)
  - [User Story 3: View a Booking Confirmation (Customer)](#user-story-3-view-a-booking-confirmation-customer)
  - [User Story 4: Modify Booking Date/Time (Customer)](#user-story-4-modify-booking-datetime-customer)
  - [User Story 5: Cancel a Booking (Customer)](#user-story-5-cancel-a-booking-customer)
  - [User Story 6: View Restaurant Menu (Customer)](#user-story-6-view-restaurant-menu-customer)
  - [User Story 7: View View Dietary Information (Customer)](#user-story-7-view-dietary-information-customer)
  - [User Story 8: Receive Email Confirmation (Customer)](#user-story-8-receive-email-confirmation-customer)
  - [User Story 9: View Booking History (Customer)](#user-story-9-view-booking-history-customer)
  - [User Story 10: Special Requests (Customer)](#user-story-10-special-requests-customer)
  - [User Story 11: View All Bookings for the Day (Staff)](#user-story-11-view-all-bookings-for-the-day-staff)
  - [User Story 12: Search Bookings by Name (Staff)](#user-story-12-search-bookings-by-name-staff)
  - [User Story 13: Mark Tables as Occupied/Available (Staff)](#user-story-13-mark-tables-as-occupiedavailable-staff)
  - [User Story 14: Update Booking Status (Staff)](#user-story-14-update-booking-status-staff)
  - [User Story 15: Manage Table Configuration (Admin)](#user-story-15-manage-table-configuration-admin)
  - [User Story 16: Manage Time Slots (Admin)](#user-story-16-manage-time-slots-admin)
  - [User Story 17: View Booking Statistics (Admin)](#user-story-17-view-booking-statistics-admin)
  - [User Story 18: Manage Menu Items (Admin)](#user-story-18-manage-menu-items-admin)
  - [Colour Palette Justification for Portuguese Restaurant Kitchen System Website](#colour-palette-justification-for-portuguese-kitchen-booking-system-website)
  - [Typography Justification for Portuguese Kitchen Booking System Website](#typography-justification-for-portuguese-kitchen-booking-system-website)
  - [Accessibility Implementation, User Flow and Navigation Strategies](#accessibility-implementation-user-flow-and-navigation-strategies)
- [References](README.md#references)

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

## Technologies Used

[⬆ Back to Table of contents](#table-of-contents)

During the development of this project, a range of tools and technologies were used to support both the design and development process.

---

### Dell Latitude 5401

This project was carried out on a Dell Latitude 5401 x64-based laptop, which features an Intel® Core™ i7-9850H processor (2.60GHz, 6 cores, 12 threads) and 16GB of RAM. This high-performance setup provides a smooth multitasking environment, fast build times, and efficient operation of development tools and browser-based testing.

---

### Windows 11 Pro

The operating system used for this project is **Windows 11 Pro**, Microsoft’s latest version of Windows. It offers enhanced security, optimised performance, and a range of developer-oriented features.

Windows 11 Pro supports advanced hardware and software integration, creating a stable and efficient environment for web development. Valuable features such as improved virtual desktops, enhanced window management, and seamless integration with Microsoft’s development tools help streamline the coding process.

In addition, Windows 11 Pro includes robust security measures such as **BitLocker encryption** and **Secure Boot**, contributing to a safe and secure development setup. Its compatibility with popular IDEs, web browsers, and validation tools—combined with regular system updates—ensures that the project can be developed and tested on a modern, dependable platform.

---

### Visual Studio Code

For the purposes of website development, **Visual Studio Code (VS Code)** is a lightweight yet powerful source code editor that enhances productivity and supports high-quality coding through a broad range of features.

During the development of this project, VS Code offered **intelligent code completion** and **syntax highlighting** for HTML5, CSS3, Javascript and Python, which improved coding speed and reduced errors. It includes built-in **Git integration** for version control, simplifying the management of commits and collaboration.

Additional extensions, such as **Live Server**, allowed for real-time previews of web pages during development, enhancing the efficiency of testing responsive design and interactive elements. Workflow preferences were customised using the interface and keyboard shortcuts, helping tailor the environment to suit development needs.

**Debugging tools** and **code linting extensions** also played a key role in promoting cleaner, error-free code. Overall, Visual Studio Code has significantly supported the organisation of the development process and the maintenance of high-quality code throughout the creation of this portfolio website.

---

### HTML5

The latest version of the HyperText Markup Language used to organise content on the web is **HTML5**. This website syntax code provides an accessible and semantic foundation, improving the clarity and organisation of the content by using meaningful elements such as `<header>`, `<nav>`, `<main>`, `<section>`, and `<footer>`.

For users relying on screen readers, these syntax tags enhance accessibility and make the site's structure easier for search engines to understand, which improves SEO. Without relying on external plugins, enabling rich media integration can be done by using multimedia elements like `<video>` and `<audio>`, which HTML also supports.

To improve user interaction and validation, HTML also includes powerful **form controls** and **attributes**. Overall, enhanced user experience, improved performance, and better cross-browser compatibility is achieved by HTML5, ensuring that the website is built on modern, standards-compliant code.

---

### CSS3

The latest development of the Cascading Style Sheets language is **CSS3**, which is used to format and visually enhance web pages.

Devices and various screen sizes benefit from a clean, professional, and smoothly adapted responsive layout through key features offered by CSS3. Regardless of the device used, an optimal user experience is ensured for desktops, tablets, and mobiles by using features such as **media queries** that support device-specific layouts.

To achieve a refined and visually engaging interface, features such as **gradients**, **shadows**, **transitions**, and **animations** are enabled by CSS3’s advanced styling capabilities.

**Distinct branding** and **consistent visual presentation** are made possible when custom CSS styling is applied to complement the structure provided by Bootstrap. A website accessible to users with visual impairments is supported through CSS3’s ability to adjust font sizes, colours, and contrast settings.

In the broader context, CSS3 plays a vital role in delivering a visually attractive, adaptive, and user-focused front-end design for this portfolio website.

---

### JavaScript (ES6+)

The **Portuguese Kitchen Booking System** utilises modern **JavaScript (ES6+)** to enhance client-side interactivity and support a responsive, user-focused booking experience. JavaScript is used to transform the application from a static website into a **dynamic, data-driven booking platform**, enabling real-time interaction between users and the reservation system.

To ensure efficient, maintainable, and scalable code, contemporary language features such as **arrow functions**, **template literals**, **modular scripting**, and **event-driven programming** are implemented in line with **ECMAScript 6 (ES6)** and later standards. These features improve performance, readability, and long-term maintainability across modern browsers and devices.

JavaScript plays a key role in managing **client-side form behaviour**, including **dynamic validation**, **date selection logic**, and **user feedback messaging** during the booking process. Immediate feedback is provided to users when submitting reservation forms, ensuring required fields are completed correctly before data is sent to the server for processing. This approach enhances usability while reducing invalid submissions and unnecessary server-side processing.

In conjunction with the back-end framework, JavaScript supports **asynchronous user interactions** that enhance the booking journey without requiring unnecessary page reloads. Interactive elements such as confirmation messages, availability indicators, and form state updates are handled smoothly, contributing to a streamlined and intuitive user experience.

To ensure accessibility and reliability across a range of devices and network conditions, the application follows **progressive enhancement principles**, allowing core booking functionality to remain usable even on lower-powered devices or slower connections (Mozilla Developer Network, 2024). All interactive features are designed to complement, rather than replace, server-side validation and processing.

Code quality and compliance with modern JavaScript standards are maintained through validation and testing using tools such as **JSHint**, helping to identify syntax issues, enforce best practices, and reduce the likelihood of runtime errors (W3C, 2023).

In summary, **JavaScript serves as a core component of the Portuguese Kitchen Booking System**, enabling responsive interactivity, enhanced form handling, and a smooth user experience. When combined with robust server-side logic and database-driven functionality, JavaScript supports the delivery of a **professional, user-centred, and fully operational restaurant booking application**, consistent with the expectations of **Level 5 Web Application Development** (Code Institute, 2025).

---

### jQuery

Within the **Portuguese Kitchen Booking System**, **jQuery** is used selectively to simplify client-side scripting tasks and enhance user interaction within the booking interface. The lightweight library supports **efficient DOM manipulation**, **event handling**, and **asynchronous requests**, contributing to a smoother and more responsive reservation experience.

jQuery is primarily applied to manage **interactive form behaviour**, **UI feedback**, and **dynamic content updates**, such as displaying confirmation messages, handling date and guest selection changes, and improving the responsiveness of booking-related components. Its concise syntax reduces code repetition and improves readability, supporting maintainable and well-structured front-end development.

To enhance usability without unnecessary page reloads, **jQuery AJAX** functionality is utilised to support asynchronous communication between the client and server where appropriate, such as submitting booking forms or updating availability-related feedback. This approach improves performance and ensures a more seamless booking journey for users by allowing real-time interaction while maintaining data integrity (jQuery Foundation, 2024).

Cross-browser compatibility is also strengthened through jQuery’s abstraction layer, ensuring consistent behaviour across modern browsers including **Chrome**, **Firefox**, **Safari**, and **Edge**. This helps reduce rendering inconsistencies and supports reliable interaction across different platforms and devices (Mozilla Developer Network, 2024).

In alignment with **progressive enhancement principles**, jQuery-based enhancements are designed to complement, rather than replace, core server-side functionality. Essential booking features remain accessible even on lower-powered devices or slower network connections, ensuring usability for a wide range of users.

In summary, jQuery plays a **supporting but valuable role** within the Portuguese Kitchen Booking System by enhancing interactivity, improving user feedback, and streamlining front-end logic. When combined with robust server-side processing and database-driven functionality, it contributes to a **professional, accessible, and user-centred restaurant booking application**, consistent with **Level 5 Web Application Development** standards (Code Institute, 2025).

---

### Jest

Within the **Portuguese Kitchen Booking System**, **Jest** is used as a testing framework to support **functional validation** and **unit testing** of client-side JavaScript logic related to the booking interface. Its implementation helps ensure that interactive components behave consistently and reliably throughout the user journey.

Jest is applied to test key front-end behaviours such as **form validation logic**, **date and guest input handling**, and **UI state changes** triggered by user interaction. By providing a structured and automated testing environment, Jest helps confirm that booking-related logic operates as intended across a range of scenarios, reducing the risk of runtime errors and unexpected behaviour (Meta Open Source, 2024).

To avoid reliance on live server responses during testing, **mock functions** are used to simulate asynchronous operations, including form submissions and client-side data handling. This approach allows logic to be tested in isolation, improving reliability and enabling early detection of logical flaws during development (Mozilla Developer Network, 2024).

Where applicable, **snapshot testing** is utilised to verify the stability of rendered UI components, ensuring that visual output and interactive elements remain consistent following code changes. This is particularly important in a booking system, where clarity, predictability, and user confidence are essential to a professional user experience.

The use of Jest aligns with **maintainable development practices** and supports long-term code quality by helping prevent regressions as features evolve. Although the core application logic is driven by server-side processing and database interactions, Jest strengthens the front-end layer by reinforcing predictable behaviour and consistent execution of JavaScript components.

Overall, the inclusion of Jest within the Portuguese Kitchen Booking System reflects a commitment to **quality assurance**, **code reliability**, and **professional development standards**, consistent with expectations for **Level 5 Web Application Development** projects (Code Institute, 2025).

---

### GitHub

A cloud-based system which includes capabilities such as collaborative development using Git and offers a version control framework.

Enabling secure and efficient tracking of modifications, managing source code revisions has been supported by using GitHub throughout this project.

I can revert to earlier iterations if required due to the functionality of being able to create repositories where the complete project history is maintained.

Without impacting the primary codebase, I could explore new concepts thanks to GitHub's branching and merging capabilities.

Also, to assist in documenting bugs or improvements, the use of GitHub's issue tracking and project management utilities proves to be a valuable skill cultivated throughout the project.

Straightforward collaboration with others is achievable as GitHub allows effortless sharing of public or private code simply by hosting the project repository.

Another advantage of GitHub is that it integrates seamlessly with Visual Studio.

During the development of this portfolio website, GitHub has been indispensable in maintaining a structured, efficient and reliable development workflow.

---

### Notepad++

For quick code editing and script authoring, at times I opted to use the versatile and lightweight text editor Notepad++.

To inspect code segments without the overhead of a full integrated development environment, Notepad++ proved to be a helpful utility throughout this project.

To enhance readability and minimise errors during manual code modifications, Notepad++'s syntax highlighting for HTML, CSS, JavaScript, and Python is a significant advantage.

To enable easy comparison and multitasking, while working concurrently on multiple files, Notepad++'s tabbed interface makes this process more manageable.

For automating repetitive actions, Notepad++ provides features that assist such as search and replace with regular expressions, auto-completion and macro recording.

Particularly for quick debugging and minor code adjustments, Notepad++'s simplicity combined with robust functionality made it a valuable complement.

---

### W3C Validator Tools

To verify the correctness of HTML and CSS code against web standards defined by the World Wide Web Consortium (W3C), the W3C Validator tools are indispensable online resources.

To enhance cross-browser consistency and accessibility and ensure that the website’s markup and styling conform to current web standards, these tools have been utilised throughout the project.

In the development process, issues relating to accessibility, obsolete elements, and syntax errors are detected and this validates HTML5 and CSS3 code.

Owing to the fact that search engines favour websites with valid and well-structured code, using W3C Validator tools assists in improving search engine optimisation (SEO).

In addition, this results in cleaner, more dependable code and an improved user experience.

To apply best practices throughout the development of this portfolio website, such as ensuring accessibility compliance and upholding code quality, W3C Validator tools proved to be invaluable.

---

### ESLint – Code Quality and Style Validation

To support clean, consistent, and maintainable JavaScript code, the **Portuguese Kitchen Booking System** implements **ESLint**, a widely adopted static analysis tool used to identify code quality issues, stylistic inconsistencies, and potential runtime errors during development.

Although the project is primarily **back-end driven**, JavaScript is still used to enhance the user experience through client-side form interaction, validation feedback, and interface behaviour. ESLint helps ensure that this supporting JavaScript remains reliable, readable, and aligned with professional coding standards.

#### Purpose of ESLint in This Project

ESLint was integrated to:

- Detect problematic JavaScript patterns and unused variables  
- Identify potential issues such as undefined variables and incorrect scope usage  
- Enforce a consistent coding style across client-side scripts related to form handling and UI interaction  
- Reduce bugs caused by syntax errors and poor code structure  
- Support professional development practices and industry-aligned code quality standards  

By applying ESLint alongside structured testing and manual validation, the project maintains a high level of **code quality**, **maintainability**, and **clarity**. This approach supports long-term scalability and aligns with expectations for **Level 5 Web Application Development**, where clean implementation and adherence to best practices are essential.

Overall, the use of ESLint within the Portuguese Kitchen Booking System reinforces a disciplined development workflow, helping to ensure that all JavaScript components contribute positively to a stable, user-focused booking experience.

---

### Bootstrap

While developing responsive and mobile-first websites, the use of Bootstrap, which is a widely used, open-source front-end framework, simplifies this process.

By utilising the adaptable grid system, pre-designed interface components, and utility classes that accelerate development and ensure a refined appearance, throughout this project, Bootstrap was significant in providing uniformity.

Responsive design capabilities have allowed the website to adapt seamlessly across desktops, tablets, and mobile devices without extensive custom CSS.

To create an intuitive and visually engaging user interface, components from Bootstrap's comprehensive library have been employed, such as navigation bars, buttons, cards, and forms.

Also worth mentioning is the assurance of the site being accessible to users with disabilities, which was facilitated by Bootstrap's integrated accessibility support features.

Considering the overall context, a smooth, user-friendly experience across devices, a professional presentation, and efficient development were effectively achieved through the use of Bootstrap.

---

### Code Institute Discord

Throughout the development of the **Portuguese Kitchen Booking System**, the **Code Institute Discord** platform was used as the primary communication and collaboration space for students and mentors on the course.

Discord enabled continuous engagement with the learning community, allowing participants to remain connected throughout the project lifecycle. Within this environment, I was able to ask questions, share progress updates, access learning resources, and receive guidance from both peers and experienced mentors.

Support related to **project development**, **problem-solving**, and **full stack implementation** was organised into clearly defined channels, making it easy to locate relevant discussions and seek targeted assistance. This structured approach helped to resolve technical challenges efficiently and encouraged knowledge sharing across the cohort.

Features such as threaded discussions, direct messaging, and file sharing supported constructive feedback and collaborative learning. These tools proved particularly valuable when troubleshooting issues related to Django configuration, database integration, and deployment.

Overall, the use of Code Institute Discord had a positive influence on the quality of the Portuguese Kitchen Booking System. The platform fostered a supportive learning environment that contributed to skill development, problem resolution, and steady project progression, reinforcing the value of collaboration within modern software development workflows.

---

### Google Meet

Another communication platform with video capabilities, Google Meet facilitated seamless virtual interaction and collaboration.

Despite geographical separation, this platform has enabled real-time engagement while attending live tutorials, mentor sessions, and group discussions.

It enables us to obtain immediate feedback from mentors or peers while reviewing course content and project progress through screen sharing.

Google Meet's reliability and intuitive interface ensure productive meetings, assisting in clarifying project specifications and resolving technical issues effectively.

Lastly, the successful development and timely delivery of this project have been supported by Google Meet’s efficient communication and collaboration.

---

### Diffchecker

To detect code differences quickly and precisely or compare text, code, and files side by side, Diffchecker is an online utility that offers these capabilities.

During the project development, this tool has proved to be very beneficial when comparing different versions of HTML, CSS, JavaScript, and Python files to ensure uniformity by easily identifying changes and spotting errors.

During the development phase, it has provided assistance in preventing accidental overwrites and verifying amendments.

Before committing code to GitHub locally, Diffchecker can facilitate debugging and version control through its practical features such as clearly highlighting additions, deletions, and modifications.

Diffchecker supports the integrity of the project's codebase progression by contributing to maintaining code standards, sharing revisions, and enhancing collaboration.

---

### Image Colour Picker

A very useful utility, Image Colour Picker enables us to select exact colour values from an image, providing HSL, RGB, and hexadecimal (HEX) codes.

To ensure a consistent and attractive colour palette across the website, this tool has been valuable for extracting precise colours from logos, design references, or photographs.

With custom CSS styling, I have sought to achieve optimal colour combinations and preserve thematic consistency.

To improve user experience through well-coordinated visual elements, the accuracy Image Colour Picker delivers has enhanced the appearance and feel of my portfolio website.

Furthermore, it removes the need for manual colour matching and eliminates guesswork, which has accelerated the design workflow.

---

### GIMP

My selected software that offers a wide range of features for graphic design, photo enhancement, image composition, as well as serving as a complement to this portfolio website, is the powerful, open-source image editor GIMP (GNU Image Manipulation Program).

I used this programme primarily for creating and editing images, optimising graphics for fast loading in browsers, and preparing assets such as logos and icons.

To help maintain quick page load times without compromising visual appeal, its comprehensive tools allow precise control over image quality and file size.

The contribution towards a clean and professional look of the website is due to GIMP's interface that enables us to work with layers, masks, and filters, which allows advanced editing and creative refinements.

---

### DALL·E

To generate images for this project, I selected the AI-driven image creation tool developed by OpenAI, called DALL·E, which produces unique, high-quality visuals based on prompts.

DALL·E has enhanced the website's aesthetic appeal without the need for stock photography or advanced graphic design expertise by creating custom visuals and imaginative artwork.

To help maintain originality and coherence in this project, DALL·E allows me to produce bespoke images tailored to the theme and content of the website.

The creative workflow is faster and enables rapid prototyping of design concepts, while enhancing engagement with distinctive graphics.

Additionally, it complements the technical aspects of frontend development effectively, contributing to a distinctive and professional online presence.

---

### Balsamiq Wireframes

For this project, I opted to create wireframes and mock-ups with the online application Balsamiq. A valuable tool, significant during the User Experience Design (UXD) Skeleton plane phase of development.

A user-friendly wireframing application that accelerates the creation process for websites. Balsamiq assisted in planning my website layout and user interface prior to the development stage.

I quickly sketched and refined design concepts, focusing on navigation, user flow, and structure.

The drag-and-drop elements and intuitive interface streamline the Skeleton plane phase, which helps identify potential usability issues early and ensures alignment with the target audience.

Planning with Balsamiq has been robust, with a clear representation of a user-focused design that translates effectively into the accessible and responsive frontend implementation.

Additionally, Balsamiq Wireframes contributed to a comprehensive workflow that enhanced understanding of the design's clarity.

---

### ChatGPT

Conversational support across a wide range of topics, including programming and web development, is what I primarily used ChatGPT, the advanced OpenAI language model, for.

Throughout the course and projects, it has assisted me by providing suggestions to enhance code quality and efficiency, explain concepts, and serve as an invaluable resource for debugging code.

ChatGPT has the capability to review my HTML, CSS, JavaScript, and Python code, where at times it identifies optimisation opportunities, logical errors, and syntax mistakes.

Additionally, it assists with generating design ideas and clarifying technical documentation.

I feel that it has accelerated problem-solving, helping me maintain focus on development challenges, overall quality, and maintainability of the website.

Throughout the project lifecycle, it has proved to be a valuable productivity tool.

---

### Microsoft Edge, Mozilla Firefox and Google Chrome

Renowned for their speed, stability, and comprehensive developer tools, Google Chrome, Mozilla Firefox and Microsoft Edge are modern, widely used web browsers.

For ensuring responsive design, all three browsers include features that allow developers to preview and test websites across a range of device resolutions and screen sizes. In the context of this project, these capabilities were used to evaluate performance across mobile, tablet, and desktop devices.

Each of these browsers offers developer tools that provide advanced debugging functionality, including live editing of HTML, CSS, and JavaScript, as well as accessibility evaluation, performance analysis, and network inspection.

Layout inconsistencies, scripting errors, and accessibility issues can therefore be efficiently detected and resolved.

Furthermore, these browsers enhance the development workflow through seamless integration with modern frameworks, version control tools, and support for developer extensions.

Using these browsers throughout the project ensured that the website was thoroughly tested and optimised for a diverse range of target users, delivering a consistent and reliable cross-device user experience.

---

## Wireframes

[⬆ Back to Table of contents](#table-of-contents)

Before progressing to visual styling or detailed interface design, **wireframes** were created to define the core structure and functionality of the **Portuguese Kitchen Booking System**. A wireframe is a simplified visual representation of a web application that focuses on layout, content hierarchy, and user flow, rather than colours, imagery, or typography.

Wireframes act as the **structural blueprint** of the application, outlining the placement of key elements such as navigation, booking forms, availability displays, and administrative controls. Presented in grayscale, they allow focus to remain on usability, clarity, and overall **user experience (UX)** without visual distraction.

As part of the **pre-production planning phase**, wireframes played a critical role in validating design decisions before development began. This ensured that functional requirements — including table reservations, form validation, and booking management — were clearly defined and agreed upon prior to implementation.

Producing wireframes for this **Milestone 3 full-stack project** reflects recognised professional practice and demonstrates a **user-centred, methodical design process**. They served as the conceptual foundation for the system, guiding both front-end structure and back-end feature integration throughout development.

### Design Rationale and Planning

The wireframes illustrate a considered approach to **information architecture, layout consistency, and booking workflow design**. By visualising user interactions at an early stage, the project was broken down into logical development phases, enabling effective planning and prioritisation of user needs.

This approach ensured that critical functionality — such as viewing availability, submitting reservations, and receiving confirmation feedback — was intuitive and clearly positioned within the interface. Presenting wireframes as part of the project highlights the importance of **planning and iterative refinement**, rather than focusing solely on the final visual outcome.

### UX Awareness

A strong emphasis on **user experience (UX)** informed all wireframe decisions. Key user journeys, particularly the **table reservation process**, were designed to minimise friction and reduce cognitive load. By focusing on flow and functionality before development, potential usability issues were identified and resolved early.

Wireframes also enabled constructive reflection and refinement during the conceptual stage, helping to reduce the need for later rework. This reinforces a commitment to delivering a **clear, accessible, and user-friendly booking system**, aligned with real-world restaurant workflows and **professional full-stack development standards**.

---

## Portuguese Kitchen Booking System Wireframes

[⬆ Back to Table of contents](#table-of-contents)

The wireframes presented here correspond to the ten pages planned for inclusion in this Portuguese Kitchen Booking System website. Each page is shown in three versions: desktop, tablet, and mobile.

---

### Homepage

The Portuguese Kitchen Booking System has been designed to provide a simple, reliable, and user-friendly way to reserve tables online. This homepage introduces visitors to the purpose and vision of the platform, establishing its role as a modern restaurant booking solution tailored to both customers and restaurant staff.

The primary aim of the website is to make the table reservation process clear, accessible, and efficient, allowing users to plan their dining experience with confidence. By presenting essential information clearly and guiding users through an intuitive booking journey, the system ensures a smooth and enjoyable experience from arrival to confirmation.

The project focuses on delivering modern web functionality, secure data handling, and a responsive design, while maintaining a welcoming and professional tone. Through clarity, usability, and trust-focused features, visitors quickly understand how the system supports restaurant reservations and why it has been developed as a practical, real-world booking platform.

<details>
<summary><strong>View wireframes (Desktop / Tablet / Mobile)</strong></summary>

**Desktop**  
<img width="673" height="817" alt="home-desktop" src="https://github.com/user-attachments/assets/f4cf89db-b726-4b05-9567-cf99e798e43e" />

**Tablet**  
<img width="673" height="1345" alt="home-tablet" src="https://github.com/user-attachments/assets/b973b873-c380-495f-8d1e-eb4d165c01ec" />

**Mobile**  
<img width="511" height="1996" alt="home-mobile" src="https://github.com/user-attachments/assets/cf7f2173-56d4-4fc0-b65e-bc4314549457" />

</details>

---

### Menu

The Menu page presents a clear and focused overview of the Portuguese Kitchen’s food offering, displaying two starters, two main dishes, and two desserts, each with descriptions and prices. The layout is intentionally simple, allowing users to quickly understand the restaurant’s cuisine before making a reservation.

A consistent top navigation menu enables seamless movement between the Home, Booking, and Login/Register, while the footer section provides essential information such as opening hours and contact details.

Overall, the Menu page supports the booking journey by combining clarity, accessibility, and structured content presentation, reinforcing the system's role as a practical and user-friendly restaurant booking platform.

<details>
<summary><strong>View wireframes (Desktop / Tablet / Mobile)</strong></summary>

**Desktop**  
<img width="673" height="1465" alt="menu-desktop" src="https://github.com/user-attachments/assets/c6719182-3d1e-4f25-bb0b-5cdfa234a5db" />

**Tablet**  
<img width="673" height="1722" alt="menu-tablet" src="https://github.com/user-attachments/assets/6e238bbc-356e-4d04-9256-702dead12a09" />

**Mobile**  
<img width="327" height="3065" alt="menu-mobile" src="https://github.com/user-attachments/assets/d1c1f4ca-7456-4a5a-8f2a-d003fe3c69a0" />

</details>

---

### Registration

The User Registration page allows customers to create an account quickly and securely, enabling access to personalised features such as managing bookings and viewing reservation history. The form collects only essential information to keep the registration process clear, simple, and user-friendly.

Consistent navigation and footer elements are maintained to provide a familiar experience across the site, reinforcing usability and accessibility. Overall, this page supports the booking system by enabling secure user access while maintaining a clean and intuitive interface aligned with real-world restaurant platforms.

<details>
<summary><strong>View wireframes (Desktop / Tablet / Mobile)</strong></summary>

**Desktop**  
<img width="673" height="997" alt="registration-desktop" src="https://github.com/user-attachments/assets/278cf09d-6198-4bce-b9bc-29c751b5f559" />

**Tablet**  
<img width="673" height="1232" alt="registration-tablet" src="https://github.com/user-attachments/assets/e1be4b07-5022-4a07-b41e-5bd69381ce64" />

**Mobile**  
<img width="511" height="2049" alt="registration-mobile" src="https://github.com/user-attachments/assets/fdcc6b5a-5b9c-466b-9133-40bc1327b872" />

</details>

---

### Login

The User Login page provides registered users with secure access to their accounts, allowing them to manage reservations and interact with personalised booking features. The interface is intentionally minimal, requesting only essential credentials to ensure a quick and straightforward login process.

Consistent navigation and footer elements maintain continuity across the website, supporting ease of use and accessibility. This page reinforces the system’s secure authentication flow while preserving a clean and professional user experience.

<details>
<summary><strong>View wireframes (Desktop / Tablet / Mobile)</strong></summary>

**Desktop**  
<img width="673" height="817" alt="login-desktop" src="https://github.com/user-attachments/assets/23564553-1948-414b-9353-311c3339f1b4" />

**Tablet**  
<img width="673" height="1232" alt="login-tablet" src="https://github.com/user-attachments/assets/49d3e9c7-4c4d-4e8a-978d-76c0471ed41a" />

**Mobile**  
<img width="511" height="1929" alt="login-mobile" src="https://github.com/user-attachments/assets/f3a652ce-4a14-420c-bd86-a4890ac2459f" />

</details>

---

### Booking

The booking page allows authenticated users to make a reservation at the Portuguese Kitchen through a clear and structured booking form. Users can select a date, time, and number of guests, with availability checks provided before confirming a reservation to prevent scheduling conflicts.

The design prioritises simplicity, accessibility, and efficient user flow, guiding customers through the booking process with clear feedback and confirmation actions. Consistent navigation and footer elements ensure continuity across the site, while the booking functionality reflects real-world restaurant reservation workflows and secure data handling practices.

<details>
<summary><strong>View wireframes (Desktop / Tablet / Mobile)</strong></summary>

**Desktop**  
<img width="673" height="817" alt="book-desktop" src="https://github.com/user-attachments/assets/5467a9f8-f9db-4ac1-8443-5f11c42f8ef7" />

**Tablet**  
<img width="673" height="1054" alt="book-tablet" src="https://github.com/user-attachments/assets/1c80865f-528b-4249-8b11-6b22689049c1" />

**Mobile**  
<img width="327" height="1943" alt="book-mobile" src="https://github.com/user-attachments/assets/fa08c8b1-02c1-4dc1-82b0-1f2da8f4a53e" />

</details>

---

### User Booking History

The Booking History page allows logged-in users to view and manage their reservations in one central location. Upcoming bookings are clearly separated from past reservations, providing users with an at-a-glance overview of their dining plans.

Users can view booking details, edit existing reservations, or cancel upcoming bookings where applicable, reflecting full CRUD functionality within a real-world booking context. This page enhances user control and transparency while maintaining a clean, accessible layout consistent with the rest of the system.

<details>
<summary><strong>View wireframes (Desktop / Tablet / Mobile)</strong></summary>

**Desktop**  
<img width="673" height="785" alt="my-book-desktop" src="https://github.com/user-attachments/assets/2e0a3372-3edf-4946-b0b7-233b02976226" />

**Tablet**  
<img width="673" height="1040" alt="my-book-tablet" src="https://github.com/user-attachments/assets/14508080-deb6-4a84-b26e-416787c0f61d" />

**Mobile**  
<img width="327" height="1762" alt="my-book-mobile" src="https://github.com/user-attachments/assets/1488597f-7f5d-4e44-be11-27207dbb9951" />

</details>

---

### User Booking Details

The Booking Details page provides users with a clear and comprehensive view of an individual reservation, displaying all relevant information including date, time, number of guests, and contact details. This page supports transparency and reassurance by confirming the booking status and reference number.

Users are able to edit or cancel their reservation directly from this page, reinforcing recognisable real-world booking workflows and demonstrating full CRUD functionality within a secure, user-authenticated environment.

<details>
<summary><strong>View wireframes (Desktop / Tablet / Mobile)</strong></summary>

**Desktop**  
<img width="673" height="785" alt="details-book-desktop" src="https://github.com/user-attachments/assets/c0be2aa9-c3f9-4829-b185-70436f5ff5af" />

**Tablet**  
<img width="673" height="1040" alt="details-book-tablet" src="https://github.com/user-attachments/assets/bd5e260d-7de8-4ad9-bbe9-8ac0351bc465" />

**Mobile**  
<img width="327" height="1762" alt="details-book-mobile" src="https://github.com/user-attachments/assets/4ee3914d-282e-4ad3-8542-7a5f5d4871e1" />

</details>

---

### User Profile

The User Profile page allows authenticated users to view and update their personal information, including contact details required for managing reservations. Core account data, such as the username, is protected from modification to maintain data integrity.

This page supports a personalised user experience by displaying membership information and booking activity, reinforcing secure account management and reflecting real-world user profile functionality within a full-stack booking system.

<details>
<summary><strong>View wireframes (Desktop / Tablet / Mobile)</strong></summary>

**Desktop**  
<img width="673" height="785" alt="user-profile-desktop" src="https://github.com/user-attachments/assets/8aeade6d-722d-4807-9966-c41b051aae16" />

**Tablet**  
<img width="673" height="1040" alt="user-profile-tablet" src="https://github.com/user-attachments/assets/d8f08994-5b25-40cf-9ad6-37d8ad64d5d2" />

**Mobile**  
<img width="327" height="1656" alt="user-profile-mobile" src="https://github.com/user-attachments/assets/d18e505b-ac54-433c-a8ef-aadb7dde713d" />

</details>

---

### Admin Dashboard

The Admin Dashboard provides restaurant staff with a centralised overview of daily operations, presenting key booking statistics such as total guests, confirmed and pending reservations, and overall capacity usage.

Designed to support efficient restaurant management, the dashboard displays bookings in a structured table, allowing administrators to view booking details, monitor statuses, and take actions such as confirming, seating, or completing reservations. This page reflects real-world operational workflows, enabling staff to manage bookings clearly and effectively through a secure administrative interface.

<details>
<summary><strong>View wireframes (Desktop / Tablet / Mobile)</strong></summary>

**Desktop**  
<img width="673" height="1197" alt="admin-dashboard-desktop" src="https://github.com/user-attachments/assets/c9cf29f6-35c4-4e1c-a49e-c20d7f1be4a1" />

**Tablet**  
<img width="673" height="1397" alt="admin-dashboard-tablet" src="https://github.com/user-attachments/assets/34ebb95d-b2ec-4243-878f-f6405509daac" />

**Mobile**  
<img width="327" height="2181" alt="admin-dashboard-mobile" src="https://github.com/user-attachments/assets/79450432-1449-46d4-b2eb-fd3501b9f48e" />

</details>

---

### Admin Booking Details

The Admin Booking Details page allows authorised staff to view full reservation information in a clear and structured format. It displays key booking data, including reference number, status, date, time, guest count, and customer contact details.

This page supports efficient booking management by enabling administrators to edit, cancel, or print reservations directly from the interface. A clear navigation option back to the dashboard ensures smooth workflow continuity. The design reflects real-world restaurant operations, prioritising clarity, accuracy, and ease of use within a secure administrative environment.

<details>
<summary><strong>View wireframes (Desktop / Tablet / Mobile)</strong></summary>

**Desktop**  
<img width="673" height="927" alt="admin-book-management-desktop" src="https://github.com/user-attachments/assets/db8a3c41-174a-47db-b8d6-52f269a67a30" />

**Tablet**  
<img width="673" height="1397" alt="admin-book-management-tablet" src="https://github.com/user-attachments/assets/89105dca-db1c-4f99-9bdb-90d36e7b26d7" />

**Mobile**  
<img width="327" height="2181" alt="admin-book-management-mobile" src="https://github.com/user-attachments/assets/bba38531-85af-4766-810c-229e66f4c8f0" />

</details>

---

## User Story 1: View Available Time Slots (Customer) 
## As a customer, I want to **view available time slots** so **I can book a table at my preferred time. (must-have)**

[⬆ Back to Table of contents](#table-of-contents)

### **Acceptance Criteria:**

**AC1 – Time Slot Visibility**

- [ ] When a customer accesses the booking page and selects a valid date, a clearly presented list of available time slots for that date is displayed.

**AC2 – Availability Accuracy**

- [ ] Existing bookings are stored in the database, and when valid time slots are displayed, only those with remaining availability are shown as selectable.

**AC3 – Fully Booked Time Slots**

- [ ] When availability is displayed, any time slot that has reached its maximum number of bookings is either hidden or shown as disabled.


**AC4 – Real-Time Data Handling**

- [ ] If another booking is made for the same date and time, the availability list is updated upon reload or refresh to ensure the information displayed remains accurate.

**AC5 – User Feedback**

- [ ] If no time slots are available for the selected date, a message is displayed informing the user that no availability exists.

**AC6 – Usability and Clarity**

- [ ] When the availability list is displayed, the time slots are presented in a logical order with clear and readable formatting.

**AC7 – Accessibility**

- [ ] When a client is using assistive technologies, the available time slots are fully accessible via keyboard navigation and screen readers.

**AC8 – Error Handling**

- [ ] If a client attempts to view available time slots without selecting a date, or after selecting an invalid one, a user‑friendly validation message is displayed.

---

## User Story 2: Specify the Number of Guests (Customer)
## As a customer, I want to **specify the number of guests** so  that **the system allocates an appropriate table. (must-have)**

[⬆ Back to Table of contents](#table-of-contents)

### **Acceptance Criteria:**

**AC1 – Guest Number Input Available**

- [ ] When a client is using the booking form and viewing the reservation fields, a clearly labelled input for the number of guests is available.

**AC2 – Valid Guest Range**

- [ ] When a client enters a guest number while using the form, the system accepts only values within the permitted range.

**AC3 – Validation for Invalid Input**

- [ ] When a client enters an invalid value while attempting to submit the booking, the system displays a validation message and prevents submission.

**AC4 – Table Allocation Logic**

- [ ] When a client selects a valid number of guests and availability is verified, the system allocates a table that meets or exceeds the required capacity.

**AC5 – No Suitable Table Available**

- [ ] If no table is available to accommodate the selected number of guests at the chosen date and time, the system displays a message explaining that no suitable table is available and prompts the user to adjust their selection.

**AC6 – Data Saved Correctly**

- [ ] When a booking is successfully created and stored, the number of guests is saved in the database and displayed correctly in the booking confirmation and/or booking history.

**AC7 – Accessibility and Usability**

- [ ] When the booking form is used on various devices with assistive technologies, the guest‑number input is keyboard accessible, screen‑reader friendly, and functions reliably across mobile, tablet, laptop, and desktop.

**AC8 – Editing a Booking**

- [ ] When a client edits the number of guests in an existing booking, the system re‑validates the value and checks table‑allocation rules before saving the changes.

---

## User Story 3: View a Booking Confirmation (Customer)
## As a customer, I want to **view my booking confirmation** so that **I have a record of my reservation. (must-have)**

[⬆ Back to Table of contents](#table-of-contents)

### **Acceptance Criteria:**

**AC1 – Confirmation Displayed After Successful Booking**

- [ ] When the customer submits a valid booking request and the booking is successfully created, the system displays a booking confirmation..

**AC2 – Confirmation Contains Key Booking Details**

- [ ] When the confirmation is displayed and the client reviews it, it includes the booking reference, date, time, number of guests, and customer name.

**AC3 – Clear Success Messaging**

- [ ] When the booking confirmation is shown, the system provides a clear success message.


**AC4 – Confirmation Is Accessible Later**

- [ ] When the client has made a booking and visits My Bookings or Booking History, they can view the confirmation record for that reservation.

**AC5 – Only the Correct User Can View It**

- [ ] When the client is logged in and attempts to view a booking confirmation, they can only access confirmations belonging to their own account.

**AC6 – Confirmation Still Works After Refresh / Revisit**

- [ ] When the booking has been created and the client refreshes the confirmation page or returns to it later, the details are retrieved correctly from the database.

**AC7 – Print/Save Option Available**

- [ ] When the client is viewing a booking confirmation and wishes to keep a copy, the page provides an option to print or save it (e.g., via a CTA button or link) without breaking the layout.

**AC8 – Error Handling for Missing/Invalid Booking**

- [ ] When a booking confirmation link is invalid or the booking does not exist, the system displays a user‑friendly error message and provides a link back to the homepage.

**AC9 – Accessible and Responsive Layout**

- [ ] When the client views the confirmation on mobile, tablet, desktop, or using assistive technology, the content is responsive, keyboard‑navigable, and readable with clear heading structure.

---

## User Story 4: Modify Booking Date/Time (Customer)
## As a customer, I want to **modify my booking date/time** so that **I can adjust plans if needed. (must-have)**

[⬆ Back to Table of contents](#table-of-contents)

### **Acceptance Criteria:**

**AC1 – Edit Option Available for Existing Bookings**

- [ ] When a client is logged in and has an existing booking, they can see an option to modify the booking date and time when viewing their Booking History or Booking Details.

**AC2 – Only Own Bookings Can Be Modified**

- [ ] When a logged‑in client attempts to edit a booking, they can only modify bookings that belong to their own account.

**AC3 – Booking Eligibility Rules Enforced**

- [ ] When the client selects **Edit** and the booking is outside the permitted modification window (e.g., too close to the booking time) or has a locked status, the system prevents editing and displays a clear message explaining why.

**AC4 – Available Time Slots Shown for the Selected Date**

- [ ] When the client is editing their booking and chooses a different date, the system displays only the available time slots for that date, based on capacity rules.

**AC5 – Validation Prevents Invalid Date/Time**

- [ ] When the client submits modifications and the new date or time is invalid (e.g., a past date, outside opening hours, or fully booked), the system blocks submission and displays a clear validation message.

**AC6 – Successful Update Persists in Database**

- [ ] When the client submits a valid new date and time and the update is confirmed, the booking is updated in the database and the new details are reflected in Booking Details and Booking History.

**AC7 – Confirmation of Changes Provided**

- [ ] When the booking has been successfully updated, the system displays a confirmation message summarising the previous and updated date/time (or at minimum the updated details).

**AC8 – No Double Booking / Capacity Conflicts**

- [ ] When the client submits a new time slot that becomes unavailable due to another booking being made at the same time, the system prevents the update and prompts the client to choose another available slot.

**AC9 – Cancel Option During Edit**

- [ ] When the client is on the edit page or form and chooses **Cancel** or navigates away, no changes are saved and the original booking remains unchanged.

**AC10 – Accessible and Responsive Editing Flow**

- [ ] When the client modifies a booking on mobile, tablet, desktop, or using assistive technology, the edit form is responsive, keyboard accessible, and provides meaningful labels and error feedback.

---

## User Story 5: Cancel a Booking (Customer)
## As a customer, I want to **cancel my booking** so **I can release the table I can't attend. (must-have)**

[⬆ Back to Table of contents](#table-of-contents)

### **Acceptance Criteria:**

**AC1 – Cancel Option Available for Active Bookings**

- [ ] When a client is logged in and has an active booking, they can see a clear **Cancel Booking** option when viewing their Booking History or Booking Details.

**AC2 – Only Own Bookings Can Be Cancelled**

- [ ] When a logged‑in client attempts to cancel a booking, they can only cancel bookings that belong to their own account.

**AC3 – Cancellation Eligibility Rules Enforced**

- [ ] When the client selects **Cancel Booking** and the booking is outside the permitted cancellation window (e.g., too close to the booking time) or is already completed or cancelled, the system prevents cancellation and displays a clear explanatory message.

**AC4 – Cancellation Confirmation Required**

- [ ] When the client selects **Cancel Booking**, the system prompts for confirmation, and the client must explicitly confirm the cancellation before it is processed.

**AC5 – Booking Status Updated Correctly**

- [ ] When the client confirms the cancellation and it is processed, the booking status is updated to Cancelled in the database.

**AC6 – Table Availability Released**

- [ ] When a booking is successfully cancelled and availability is recalculated, the cancelled time slot becomes available again for other customers to book.

**AC7 – Cancellation Feedback Provided**

- [ ] When the cancellation is successful, the system displays a confirmation message indicating that the booking has been cancelled.

**AC8 – Booking History Reflects Cancellation**

- [ ] When a booking has been cancelled and the client views their Booking History, the booking is clearly marked as Cancelled and can no longer be modified.

**AC9 – No Changes Without Confirmation**

- [ ] When the client opens the cancellation flow but chooses **Cancel** or closes the confirmation dialogue, no changes are made and the booking remains unchanged.

**AC10 – Accessible and Responsive Cancellation Flow**

- [ ] When the client cancels a booking on mobile, tablet, or desktop, or when using assistive technology, the cancellation process is responsive, keyboard accessible, and provides clear labels and feedback messages.

---

## User Story 6: View Restaurant Menu (Customer)
## As a customer, I want to **view the restaurant menu** so **I can see what's offered before booking. (must-have)**

[⬆ Back to Table of contents](#table-of-contents)

### **Acceptance Criteria:**

**AC1 – Menu Page Is Accessible From Main Navigation**

- [ ] When a visitor is on any page of the website and uses the top navigation, they can access the Menu page in a single click.

**AC2 – Menu Content Displays Correctly**

- [ ] When a visitor opens the Menu page and it loads, the menu displays clearly organised sections (e.g., Starters, Mains, Desserts) with item names and prices.

**AC3 – Menu Items Include Essential Information**

- [ ] When the menu is displayed and the visitor views it, each item shows the dish name, price, and image. 

**AC4 – Menu Page Supports Booking Journey**

- [ ] When a visitor is on the Menu page and decides to reserve a table, they can navigate to the Booking page using the top navigation or a call‑to‑action button. 

**AC5 – Menu Page Works for Logged-Out and Logged-In Users**

- [ ] When a client opens the Menu page, whether logged in or not, the menu remains fully visible without restrictions. 

**AC6 – Responsive Layout Across Devices**

- [ ] When a visitor views the Menu page on mobile, tablet, or desktop, the layout adapts to the screen, and all menu sections and prices remain readable, aligned, and usable without horizontal scrolling. 

**AC7 – Accessibility Standards Followed**

- [ ] When the Menu page includes images and headings and a screen reader is used, images have appropriate alt text, headings follow a logical structure, and text contrast supports readability.

**AC8 – Error Handling for Missing Menu Data**

- [ ] When menu items are stored in the database (or rendered from templates) and the menu data is unavailable or empty, the user sees a friendly message such as “Menu currently unavailable — please check back soon” instead of a broken page. 

---

## User Story 7: View Dietary Information (Customer)
## As a customer, I want to **see dietary information** so **I can check if the menu suits my requirements. (should-have)**

[⬆ Back to Table of contents](#table-of-contents)

### **Acceptance Criteria:**

**AC1 – Dietary Information is Visible on the Menu**

- [ ] When a client is viewing the Menu page and items are displayed, each item shows clear dietary information (e.g., V for vegetarian, GF for gluten‑free, DF for dairy‑free) presented as **icons, labels,** or **short tags**.

**AC2 – Dietary Key/Legend is Provided**

- [ ] When dietary tags or icons are used and the customer views the menu, a **legend or key** is available explaining what each dietary label means.

**AC3 – Allergens are Clearly Identified**

- [ ] When a customer has allergy concerns and views the menu, items display **relevant allergen information** (e.g., contains milk, eggs, fish, nuts) or include a **‘Contains allergens’ indicator** with details available.

**AC4 – Information is Accurate and Consistent**

- [ ] When dietary information is displayed across the menu and the customer compares items, **labels are applied consistently** using the same rules (e.g., “GF” only used when the dish is genuinely gluten‑free, not “can be made GF” unless stated).

**AC5 – Optional Filtering (If Implemented)**

- [ ] When the menu includes dietary filters and the customer selects a filter (e.g., “Vegetarian” or “Gluten‑Free”), only **matching items** are shown (or clearly highlighted), and the filter can be removed to return to the full menu.

**AC6 – Accessible Presentation**

- [ ] When a client uses assistive technology to navigate the menu, dietary labels or icons are **readable**, include accessible text (not colour‑only), and can be interpreted by **screen readers** (e.g., via aria‑labels or visible text).

**AC7 – Mobile Responsiveness**

- [ ] When a customer views the menu on mobile or tablet and the layout adjusts, **dietary tags remain visible** and do not overlap prices, titles, or descriptions.

**AC8 – Missing Data Handling**

- [ ] When an item does not yet have dietary information recorded and the customer views that item, the system displays a **clear fallback message** such as “Dietary info not available” rather than showing incorrect or blank labels.

---

## User Story 8: Receive Email Confirmation (Customer)
## As a customer, I want to **receive email confirmation** so that **I have proof of my booking. (could-have)**

[⬆ Back to Table of contents](#table-of-contents)

### **Acceptance Criteria:**

**AC1 – Confirmation Email is Sent After Successful Booking**

- [ ] When a client successfully makes a booking and it is confirmed by the system, an email confirmation is automatically sent to the address provided during booking.

**AC2 – Email Contains Essential Booking Details**

- [ ] When a confirmation email is sent and the client opens it, it includes:

- restaurant name

- booking reference number

- date and time of the reservation

- number of guests

- customer name

- restaurant contact details or location

**AC3 – Clear and Professional Email Format**

- [ ] When the confirmation email is sent and the client reads it, the message is clearly structured, professionally written, and easy to understand.


**AC4 – Email Matches Stored Booking Data**

- [ ] When the booking exists in the database and the confirmation email is generated, all details in the email match the saved booking record exactly.

**AC5 – Email Delivery Failure Handling**

- [ ] When the email cannot be delivered (e.g., invalid email address or mail server issue) and the system detects the failure, the booking remains confirmed and the system logs the error or displays a suitable notification for administrators.

**AC6 – Confirmation is Sent Only Once per Booking**

- [ ] When a booking is created successfully, the client receives only one confirmation email for that booking (unless the booking is later modified or intentionally resent).

**AC7 – Accessibility and Readability**

- [ ] When a client uses assistive technologies and reads the email on different devices or via a screen reader, the content is readable, uses plain text or accessible HTML, and does not rely on images alone.

**AC8 – Timely Delivery**

- [ ] When a booking is confirmed and the system sends the confirmation email, it is dispatched immediately or within a reasonable timeframe (e.g., within a few minutes).

---

## User Story 9: View Booking History (Customer)
## As a customer, I want to **view my booking history** so **I can track past visits. (should-have)**

[⬆ Back to Table of contents](#table-of-contents)

### **Acceptance Criteria:**

**AC1 – Booking History Is Available to Logged-In Users**

- [ ] When the client is logged in and navigates to My Bookings or Booking History, they can view a list of their bookings.

**AC2 – Booking History Shows Only the Customer’s Own Bookings**

- [ ] When the client is logged in and the booking history is displayed, it shows only bookings linked to that user account and not those of other users.

**AC3 – Bookings Are Displayed in a Clear, Structured Format**

- [ ] When bookings exist for the client and the booking history page loads, each booking is shown with key details such as:
- booking reference/ID
- date and time
- number of guests
- status (e.g., Confirmed / Cancelled / Completed)

**AC4 – Sorting Supports Tracking Past Visits**

- [ ] When the booking history list is displayed, bookings are ordered in a logical way (e.g., most recent first) to help clients track past visits easily.

**AC5 – Past vs Upcoming Bookings are Clearly Identified**

- [ ] When the booking history contains a mix of dates, it is clear which bookings are upcoming and which are in the past (e.g., via labels, status, or sectioning).

**AC6 – Empty State Messaging**

- [ ] When the client has no bookings and opens the booking history page, a clear message is shown (e.g., “You have no bookings yet”), along with a link or button to make a new booking.

**AC7 – Access to Booking Details from History**

- [ ] When the client views their list of bookings and selects one (e.g., “View details”), they are taken to a booking‑detail view showing full information for that reservation.

**AC8 – Responsive and Accessible Display**

- [ ] When the client views their booking history on mobile, tablet, or desktop, the page remains readable and usable across screen sizes and follows accessibility best practice (keyboard navigation, readable contrast, semantic structure).

---

## User Story 10: Special Requests (Customer)
## As a customer, I want to **add special requests** so that **I can check if the menu suits my requirements. (could-have)**

[⬆ Back to Table of contents](#table-of-contents)


### **Acceptance Criteria:**

**AC1 – Special Requests Field is Available during Booking**

- [ ] When the client is making a booking and viewing the booking form, they can see a **Special Requests** input field (e.g., a text area).

**AC2 – Special Requests Are Optional**

- [ ] When the client completes the booking form and leaves the **Special Requests** field blank, the booking can still be submitted successfully.

**AC3 – Special Requests are Saved with the Booking**

- [ ] When the client enters a special request and submits the booking form, the request is stored and linked to that booking in the database.

**AC4 – Input is Validated and Limited**

- [ ] When the client enters text into the **Special Requests** field and submits the booking, the system validates the input (e.g., maximum character limit) and displays a clear error message if the limit is exceeded.

**AC5 – Special Requests are Visible in Booking Confirmation**

- [ ] When the booking is successfully created and the customer views the confirmation page, their special request is displayed as part of the booking summary (or shown as "None" if not provided).

**AC6 – Special Requests are Visible in Booking History/Details**

- [ ] When the customer views their booking history or booking details and opens a specific booking, the special request (if provided) is displayed.

**AC7 – Special Requests can be Updated when Editing a Booking**

- [ ] When the client edits an existing booking (where editing is allowed) and updates the **Special Requests** field before saving changes, the updated request is stored and displayed in the booking details.

**AC8 – Admin can View Special Requests**

- [ ] When an administrator or staff member views a booking in the admin dashboard and opens the booking record, the **Special Requests** information is visible to support service preparation.

**AC9 – Secure Handling of User Input**

- [ ] When the client submits special‑request text and the system stores and displays it, the input is handled securely (e.g., sanitised or escaped) to prevent malicious content from being executed.

---

## User Story 11: View All Bookings for the Day (Staff)
## As a staff member, I want to **view all bookings for today** so that **I can prepare tables. (must-have)**

[⬆ Back to Table of contents](#table-of-contents)

### **Acceptance Criteria:**

**AC1 – Staff-Only Access**

- [ ] Access is restricted to staff or admin users when a logged‑in user attempts to view today’s bookings. 

**AC2 – Display Today’s Bookings Automatically**

- [ ] All bookings for the current date are shown by default when a staff member opens the bookings dashboard.

**AC3 – Relevant Booking Information Is Shown**

- [ ] When today’s bookings are displayed, each entry includes:

- booking time

- number of guests

- customer name

- special requests (if any)

- booking status (e.g., confirmed, cancelled)


**AC4 – Bookings Are Ordered by Time**

- [ ] Bookings are listed in chronological order when multiple bookings exist for the day.

**AC5 – No Bookings Message**

- [ ] A clear message is displayed when no bookings exist for today.

**AC6 – Real-Time or Refreshed Data**

- [ ] **The list reflects the latest booking data** when a booking is created, updated, or cancelled and the page is refreshed (or auto‑refreshed, if implemented).

**AC7 – Visual Clarity for Preparation**

- [ ] Bookings are presented in a clear, readable layout that supports quick staff preparation (e.g., spacing, labels, emphasis on time and guest count).

**AC8 – Time Zone Accuracy**

- [ ] **Booking times reflect the restaurant’s local time** when today’s bookings are displayed.

**AC9 – Secure Data Handling**

- [ ] **Only necessary customer information is shown and handled securely** in accordance with data‑protection practices.

---

## User Story 12: Search Bookings by Name (Staff)
## As a staff member, I want to **search bookings by name** so that **I can quickly find customer reservations. (must-have)**

[⬆ Back to Table of contents](#table-of-contents)

### **Acceptance Criteria:**

**AC1 – Staff-Only Access**

- [ ] When a user is logged in and attempts to access the booking search functionality, the feature is available only to staff or admin users.

**AC2 – Search Input Availability**

- [ ] When a staff member is on the bookings management page and the page loads, a clearly visible search input field is available for entering a customer name.

**AC3 – Case-Insensitive Name Search**

- [ ] When a staff member enters a customer name (full or partial) and submits the search, the system returns bookings that match the name regardless of letter case.

**AC4 – Partial Match Support**

- [ ] When a staff member enters part of a customer’s name and performs a search, all bookings containing the matching text in the customer name are displayed.

**AC5 – Search Results Accuracy**

- [ ] When a search query is submitted and results are displayed, only bookings that match the entered customer name are shown.

**AC6 – Clear Results Presentation**

- [ ] When matching bookings are found and results are displayed, each booking includes key information such as:

- customer name

- booking date

- booking time

- number of guests

- booking status

**AC7 – No Results Feedback**

- [ ] When no bookings match the search criteria and the search is executed, a clear message is displayed indicating that no matching bookings were found.

**AC8 – Reset or Clear Search**

- [ ] When a staff member has performed a search and then clears the search input or selects a reset option, the full bookings list is restored.

**AC9 – Performance and Responsiveness**

- [ ] When a large number of bookings exist and a staff member performs a search, results are returned quickly without noticeable delay.

**AC10 – Secure Handling of Search Data**

- [ ] When client data is searched and displayed, only authorised staff can view the information, and it is handled securely in line with data‑protection requirements.

---

## User Story 13: Mark Tables as Occupied/Available (Staff)
## As a staff member, I want to **mark tables as occupied/available** so that **booking status is current. (should-have)**

[⬆ Back to Table of contents](#table-of-contents)

### **Acceptance Criteria:**

**AC1 – Staff-Only Access**

- [ ] When a user is logged in and accesses table‑management features, only staff or admin users can mark tables as occupied or available.

**AC2 – Table Status Visibility**

- [ ] When a staff member views the table or bookings management page and it loads, each table clearly displays its current status (e.g., Available or Occupied).

**AC3 – Ability to Update Table Status**

- [ ] When a staff member selects a table and chooses to update its status, they can mark the table as either Occupied or Available.

**AC4 – Real-Time Status Update**

- [ ] When a table’s status is changed and the update is confirmed, the new status is applied immediately and reflected in the system.

**AC5 – Booking Status Synchronisation**

- [ ] When a table is marked as Occupied and it is linked to an active booking, the associated booking status is updated accordingly (e.g., In Use).

**AC6 – Prevention of Conflicting Bookings**

- [ ] When a table is marked as Occupied while new bookings are being made, the system prevents that table from being assigned until it is marked as Available again.

**AC7 – Visual Status Indicators**

- [ ] When tables are displayed in the system and their status changes, clear visual indicators (such as colour coding or icons) reflect the current state.

**AC8 – Confirmation Feedback**

- [ ] When a staff member updates a table’s status and the action is completed, a confirmation message is displayed to indicate the update was successful.

**AC9 – Error Handling**

- [ ] When an error occurs while updating a table’s status and the system cannot complete the action, a clear error message is shown and the previous status remains unchanged.

**AC10 – Audit and Accountability (Optional)**

- [ ] When a table’s status is changed and the update is saved, the system records which staff member made the change and when, for tracking purposes.

---

## User Story 14: Update Booking Status (Staff)
## As a **staff member**, I want to **update booking status** (confirmed, seated, completed) so that **I can track the booking lifecycle. (should-have)**

[⬆ Back to Table of contents](#table-of-contents)

### **Acceptance Criteria:**

**AC1 – Staff-Only Access**

- [ ] When a user is logged in and attempts to update a booking status, only staff or admin users can perform the action.

**AC2 – Status Is Visible on Booking Records**

- [ ] When a staff member views the bookings list or booking‑detail page and booking information is displayed, the current status (e.g., Confirmed, Seated, Completed) is clearly shown for each booking. 

**AC3 – Allowed Status Options**

- [ ] When a staff member updates a booking and opens the status control, they can select only from the allowed statuses: Confirmed, Seated, Completed. 

**AC4 – Valid Status Progression**

- [ ] When a booking already has a status and a staff member changes it, the system enforces logical progression (e.g., Confirmed - Seated - Completed) and prevents invalid transitions (e.g., Completed - Seated). 

**AC5 – Status Update Saves Successfully**

- [ ] When a staff member selects a new status and submits the change, and the system processes the update, the new status is saved to the database and persists after a page refresh. 

**AC6 – Immediate UI Feedback**

- [ ] When a booking status is updated and the update completes, the staff member sees an immediate confirmation message and the updated status is reflected clearly in the interface. 

**AC7 – Booking List Reflects Updates**

- [ ] When a booking status has been updated and the staff member returns to the bookings list, the list shows the updated status for that booking. 

**AC8 – Error Handling and Data Integrity**

- [ ] When an error occurs during a status update (e.g., server failure, validation issue) and the system cannot save the change, an error message is displayed and the booking status remains unchanged. 

**AC9 – Audit Trail**

- [ ] When a booking status is updated and the change is saved, the system records who made the change and when (e.g., “Updated by [staff user] on [date/time]”). 

**AC10 – Filtering and Search Compatibility**

- [ ] When bookings can be filtered or searched and a staff member filters by status (e.g., show Seated bookings), bookings appear correctly according to their current saved status. 

---

## User Story 15: Manage Table Configuration (Admin)
## As an **admin**, I want to **manage table configuration** so that **I can adjust capacity and availability. (should-have)**

[⬆ Back to Table of contents](#table-of-contents)

### **Acceptance Criteria:**

**AC1 – Admin-Only Access**

- [ ] When a user is logged in and accesses table‑configuration settings, only users with admin privileges can view or modify the configuration. 

**AC2 – View Existing Table Configuration**

- [ ] When an admin opens the table‑management area and the page loads, all tables are displayed with key details (e.g., table ID/number, capacity, current availability status). 

**AC3 – Create New Tables**

- [ ] When an admin is managing tables and adds a new table, they must be able to define at minimum:

- table identifier (number/name)

- seating capacity

- initial availability status

- immediate visibility after creation

**AC4 – Update Table Capacity**

- [ ] When an existing table is selected and the admin updates its seating capacity, the new capacity is validated (positive integer) and saved successfully.

**AC5 – Manage Table Availability Status**

- [ ] When a table exists and the admin changes its availability status, it can be marked as **Available** or **Unavailable**, and unavailable tables cannot be allocated to new bookings.

**AC6 – Prevent Conflicting Changes**

- [ ] When a table is currently assigned to an active booking and the admin attempts to reduce its capacity below the booked guest count or mark it unavailable, the system prevents the change and displays a clear warning message.

**AC7 – Persist Configuration Changes**

- [ ] When an admin saves table‑configuration changes and the page is refreshed or revisited, all changes persist correctly in the database.

**AC8 – Capacity Reflected in Booking System**

- [ ] When table configuration has been updated and customers search for availability, the booking system reflects the updated capacity and availability rules.

**AC9 – Confirmation and Feedback**

- [ ] When an admin successfully updates table configuration and the action completes, a confirmation message is displayed indicating the changes were saved.

**AC10 – Error Handling**

- [ ] When an error occurs during table‑configuration updates and the system cannot save the changes, an error message is shown and no partial updates are applied.

**AC11 – Delete or Disable Tables**

- [ ] When an admin no longer needs a table and chooses to delete or disable it, the system confirms the action and ensures the table is removed from future booking availability without affecting historical records.

**AC12 – Audit Logging**

- [ ] When a table‑configuration change is made and the update is saved, the system records who made the change and when, for administrative tracking.

---

## User Story 16: Manage Time Slots (Admin)
## As an **admin**, I want to **manage time slots** so that **I can control when bookings are accepted. (must-have)**

[⬆ Back to Table of contents](#table-of-contents)

### **Acceptance Criteria:**

**AC1 – Admin-Only Access**

- [ ] When a user is logged in and attempts to access time‑slot management, only users with admin privileges can view or edit time slots.

**AC2 – View Existing Time Slots**

- [ ] When an admin opens the time‑slot management page and it loads, all configured time slots are displayed (e.g., start time, end time or duration, active/inactive status, applicable days).

**AC3 – Create New Time Slots**

- [ ] When an admin is managing time slots and adds a new one, they must be able to set at minimum:

- start time

- end time or duration

- applicable days (e.g., Mon–Sun)

- active status

- immediate saving and display 

**AC4 – Edit Time Slots**

- [ ] When a time slot exists and the admin edits it (time, days, active status), the updated values are validated and saved successfully.

**AC5 – Enable/Disable Time Slots**

- [ ] When a time slot exists and the admin marks it as inactive, the slot is no longer available to customers when booking, while existing bookings for that slot remain unchanged.

**AC6 – Prevent Duplicate or Overlapping Slots**

- [ ] When an admin creates or edits a slot and it overlaps with or duplicates another active slot for the same day(s), the system prevents saving and displays a clear error message.

**AC7 – Booking Form Uses Active Time Slots Only**

- [ ] When customers make a booking and the booking form loads available times, only active time slots for the selected date or day are shown.

**AC8 – Respect Restaurant Opening Times**

- [ ] When restaurant opening and closing hours are configured and an admin creates or edits a time slot, the system prevents slots outside opening hours and provides feedback.

**AC9 – Capacity Awareness per Slot**

- [ ] When capacity rules (tables or seat limits) are configured and customers choose a time slot, the system offers the slot only if capacity is available for the selected party size.

**AC10 – Persist Changes**

- [ ] When an admin saves changes to time slots and later revisits or refreshes the page, the saved time slots remain correct and consistent.

**AC11 – Confirmation and Feedback**

- [ ] When an admin successfully adds, updates, or disables a time slot and the action completes, a success message confirms the change.

**AC12 – Error Handling**

- [ ] When a save operation fails (due to validation errors or system issues) and the admin submits changes, the system displays a clear error message and does not apply partial updates.

**AC12 – Audit Logging**

- [ ] When an admin makes a change to time slots and the update is saved, the system records who made the change and when, for accountability.

---

## User Story 17: View Booking Statistics (Admin)
## As an **admin**, I want to **view booking statistics** so that **I can analyse restaurant usage patterns. (should-have)**

[⬆ Back to Table of contents](#table-of-contents)

### **Acceptance Criteria:**

**AC1 – Admin-Only Access**

- [ ] When a user is logged in and attempts to access booking statistics, only users with admin privileges can view the statistics dashboard.

**AC2 – Statistics Dashboard Availability**

- [ ] When an admin opens the booking‑statistics page and it loads, the system displays an overview of statistics without errors and within a reasonable time.

**AC3 – Date Range Filtering**

- [ ] When an admin views booking statistics and selects a date range (e.g., last 7 days, last 30 days, custom range), all displayed statistics update to reflect only bookings within that range.

**AC4 – Core Metrics Displayed**

- [ ] When an admin views the dashboard and statistics are shown, the following metrics are displayed at minimum:

- total bookings

- total guests (sum of party sizes)

- cancelled bookings count

- completed bookings count (if status tracking exists)

**AC5 – Usage Pattern Insights**

- [ ] When an admin views statistics for a date range, the dashboard displays at least one usage‑pattern view such as:

- bookings by day of week

- bookings by time slot

**AC6 – Status Breakdown (If Status Exists)**

- [ ] When booking statuses exist (e.g., confirmed, seated, completed, cancelled) and the admin views the dashboard, bookings are broken down by status for the selected date range.

**AC7 – Data Accuracy and Consistency**

- [ ] When bookings exist in the database and an admin compares statistics with the booking list for the same date range, totals and breakdowns match the underlying records.

**AC8 – Handles No-Data Scenarios**

- [ ] When there are no bookings in the selected date range and the admin views statistics, the dashboard displays “No data available for this period” (or equivalent) and shows zeros rather than errors.

**AC9 – Real-Time / Recently Updated Data**

- [ ] When an admin creates, updates, or cancels a booking and then revisits or refreshes the statistics page, the dashboard reflects the updated data.

**AC10 – Accessible Presentation**

- [ ] When an admin uses assistive technologies to view charts or tables, the statistics are readable and accessible (clear headings, meaningful labels, sufficient contrast), and key metrics are available in text form rather than charts alone.

**AC11 – Performance for Large Data Sets**

- [ ] When a large number of booking records exist and the admin loads statistics for a broad date range, the page remains responsive and loads within a reasonable time (e.g., caching or aggregation used where appropriate).

**AC12 – Export/Download Option (Optional Enhancement)**

- [ ] When an admin chooses to export records (if implemented), the system downloads the statistics in a usable format (e.g., CSV) matching the selected date range.

---

## User Story 18: Manage Menu Items (Admin)
## As an **admin**, I want to **manage menu items** so that **customers see current offerings. (could-have)**

[⬆ Back to Table of contents](#table-of-contents)

### **Acceptance Criteria:**

**AC1 – Admin-Only Access**

- [ ] When a user is logged in and accesses the menu‑management area, only users with admin privileges can access it; non‑admin users are denied or redirected.

**AC2 – View Menu Items List**

- [ ] When an admin opens the menu‑management page and it loads, a list or table of existing menu items is displayed (e.g., name, category, price, availability status).

**AC3 – Add a New Menu Item**

- [ ] When an admin is on the menu‑management page and submits a valid "Add menu item" form, the new item is saved to the database and appears in the admin list.

**AC4 – Required Field Validation**

- [ ] When an admin creates or edits a menu item and required fields are missing or invalid, the form does not submit and clear validation messages are shown.

- required‑field validation

Minimum required fields typically include:

- item name

- category (e.g., starter, main, dessert)

- price

**AC5 – Edit an Existing Menu Item**

- [ ] When an admin selects an existing menu item, updates its details, and saves, the changes are stored and immediately reflected in the admin list.

**AC6 – Delete a Menu Item**

- [ ] When an admin chooses to delete a menu item and confirms the deletion, the item is removed from the database and no longer appears to customers.

**AC7 – Control Customer Visibility (Available / Hidden)**

- [ ] When an admin manages menu items and marks an item as available or hidden/unavailable, only available items appear on the customer‑facing menu page.

**AC8 – Category Display on Customer Menu**

- [ ] When menu categories exist (starters, mains, desserts, etc.) and customers view the menu page, items are displayed under the correct category based on the admin‑set category field.

**AC9 – Price Formatting**

- [ ] When an admin enters a price and the item is displayed to customers, the price appears in a consistent currency format (e.g., £12.50) and is stored accurately.

**AC10 – Image Handling (If Implemented)**

- [ ] When menu images are supported and an admin uploads or assigns an image to a menu item, the image displays correctly on customer menu tiles, and invalid file types or sizes are rejected with a clear error.

**AC11 – Data Integrity and Safe Deletion**

- [ ] When an admin deletes or hides an item and the customer menu loads, the menu page remains functional with no broken links, missing images, or server errors.

**AC12 – Accessibility and Usability**

- [ ] When admins or customers use assistive technologies to view menu‑management forms or the customer menu, pages use clear labels, meaningful validation feedback, and accessible navigation (keyboard‑friendly and readable).

---

## Colour Palette Justification for Portuguese Kitchen Booking System Website

[⬆ Back to Table of Contents](#table-of-contents)

### Chosen Colour Palette

| Colour Name     | Hex Code  | Usage                                                                 |
|-----------------|-----------|-----------------------------------------------------------------------|
| Azulejo Blue    | `#1F4E79` | Primary brand colour; navigation bar, header sections, and key accents |
| Olive Green     | `#6B8E23` | Secondary tone; section dividers, icons, and subtle highlights        |
| Terracotta Red  | `#C44536` | Call-to-action buttons, booking actions, and interactive elements     |
| Linen Cream     | `#FAF7F2` | Main background colour providing warmth and visual comfort            |
| Espresso Brown  | `#3A2F2A` | Headings, body text, and footer background                             |
| Porcelain White | `#FFFFFF` | Card backgrounds, forms, and modal components   

### Overview and Rationale

To reflect the warmth, authenticity, and cultural richness of Portuguese cuisine, the colour palette for the Portuguese Kitchen Booking System website has been carefully selected to evoke comfort, tradition, and trust while maintaining a contemporary digital aesthetic (Agrawal, 2025; Baradell, 2023; DesigningIt, 2024).

As the platform supports core interactions such as table reservations, menu browsing, and customer enquiries, the palette balances inviting warmth with professional clarity. Earth-inspired tones echo traditional Portuguese kitchens and Mediterranean dining culture, while clear contrast and hierarchy support usability and accessibility across devices.

### Justification

**Cultural Blue for Trust and Identity**

Azulejo Blue (`#1F4E79`) draws inspiration from traditional Portuguese *azulejo* tiles, reinforcing cultural identity while conveying trust, reliability, and professionalism (Baradell, 2023; DesigningIt, 2024). As the primary brand colour, it anchors navigation elements and headers, giving users confidence when booking tables or submitting personal details.

**Warm Accents to Encourage Bookings**

Terracotta Red (`#C44536`) is used strategically for call-to-action buttons such as **“Book a Table”** and **“Confirm Reservation.”** This colour references traditional clay cookware and Mediterranean warmth, creating a sense of appetite, urgency, and engagement without overwhelming the interface (Agrawal, 2025; DesigningIt, 2024).

**Natural Tones for Comfort and Atmosphere**

Olive Green (`#6B8E23`) subtly reinforces associations with fresh ingredients, olive oil, and authentic Portuguese cooking. Used sparingly for icons and separators, it enhances visual interest while maintaining harmony with the warmer tones (Baradell, 2023).

**Neutral Foundation for Readability and Accessibility**

Linen Cream (`#FAF7F2`) and Porcelain White (`#FFFFFF`) provide a calm, uncluttered foundation that allows menus, booking forms, and imagery to stand out clearly. These tones reduce visual fatigue and support extended reading, particularly when users browse menus or reservation details (DesigningIt, 2024).

**Professionalism and Legibility through Espresso Brown**

Espresso Brown (`#3A2F2A`) is applied to headings and body text to ensure strong contrast and comfortable readability. Dark but warm, it avoids the harshness of pure black while meeting WCAG contrast requirements for accessible typography (W3C, 2023).

### Consistent Branding and Hierarchical Balance

The six-colour palette establishes a cohesive visual hierarchy across navigation bars, booking forms, menu cards, and confirmation screens. Primary and accent colours guide user attention, while neutral tones ensure balance and visual stability. This consistency reinforces brand recognition and supports a polished, professional user experience aligned with modern restaurant booking platforms (DesigningIt, 2024).

### Applied Colour Theory Principles

**1. Analogous Harmony**

Warm earth tones (Terracotta Red, Espresso Brown, Linen Cream) are naturally harmonised with Olive Green, reflecting the organic, food-centred nature of the brand and creating a welcoming dining atmosphere (Baradell, 2023).

**2. Complementary Contrast**

Azulejo Blue is complemented by warm Terracotta Red accents, effectively directing user focus toward interactive elements such as booking actions and confirmations (Agrawal, 2025).

**3. Psychological Impact**

Warm colours stimulate appetite and comfort, while blue tones reinforce trust and professionalism—an essential balance for a food-based transactional website (Agrawal, 2025; Baradell, 2023).

**4. Accessibility and Readability**

High-contrast text-to-background pairings ensure compliance with WCAG 2.1 guidelines. Light backgrounds support dark typography, ensuring clarity across different screen sizes and lighting conditions (W3C, 2023).

**5. Visual Consistency and Brand Recognition**

The palette is consistently applied across all components, including cards, modals, forms, and navigation. Combined with Bootstrap 5 and custom CSS variables, this approach ensures a responsive and recognisable brand identity across devices (Bootstrap, 2024; DesigningIt, 2024).

### Strategic Use of Colour

- **Emphasis**: Booking and confirmation buttons use Terracotta Red (`#C44536`) to encourage action  
- **Hierarchy**: Azulejo Blue (`#1F4E79`) for navigation and section headings; Espresso Brown (`#3A2F2A`) for body text  
- **Consistency**: The defined palette is applied uniformly across menus, booking flows, and UI components  
- **Balance**: Olive Green (`#6B8E23`) introduces subtle contrast without visual overload  
- **Contrast**: Linen Cream (`#FAF7F2`) and Porcelain White (`#FFFFFF`) provide clear separation from text and controls  

### Summary

The Portuguese Kitchen Booking System website employs a culturally informed and psychologically balanced colour palette to create a warm, trustworthy, and accessible user experience. By combining Mediterranean earth tones with traditional Portuguese blue accents, the interface reflects the brand’s culinary identity while supporting modern usability principles (Interaction Design Foundation, 2023; DesigningIt, 2024).

This considered use of colour enhances user confidence during the booking process, supports accessibility, and reinforces a cohesive brand presence—ensuring the platform feels both authentic and professional within a competitive digital restaurant landscape.

---

## Typography Justification for Portuguese Kitchen Booking System Website

[⬆ Back to Table of contents](#table-of-contents)

### Overview

For the Portuguese Kitchen Booking System website, the typography has been carefully selected to support a welcoming, professional, and trustworthy dining experience while ensuring accessibility and clarity for all users (99designs, 2024; Google Fonts, 2024; DesigningIt, 2024).

The target audience includes restaurant customers such as couples, families, local diners, and tourists seeking an authentic Portuguese dining experience. As the platform facilitates key interactions including table reservations, menu browsing, and customer enquiries, the chosen typography prioritises readability, warmth, and usability across devices (99designs, 2024; DesigningIt, 2024).

The selected typeface pairing—Montserrat for headings and Lato for body text—reflects modern web design conventions commonly used in hospitality and booking systems. This combination balances contemporary aesthetics with approachability, reinforcing the brand’s culinary identity while remaining highly legible and accessible (Google Fonts, 2024; DesigningIt, 2024).

### Typography Goals

The chosen combination of typefaces was selected to ensure the website is:

- Easy to read and accessible for all users
- Professional and trustworthy for transactional interactions such as bookings
- Warm, friendly, and appropriate for a food and hospitality context
- Fully responsive and legible across all screen sizes and devices
- Flexible enough to support longer content such as menus, booking forms, confirmations, and informational pages  

This approach aligns with recognised UX and accessibility best practices (Interaction Design Foundation, 2023; Google Fonts, 2024; DesigningIt, 2024).

### Primary Typeface – Montserrat (Headings)

The geometric sans-serif typeface **Montserrat** is used for all primary headings, section titles, navigation items, feature labels, and call-to-action text.

**Justification:**  
Montserrat’s clean lines, balanced proportions, and structured appearance establish a clear visual hierarchy, allowing users to quickly scan important information such as page titles, menu categories, and booking actions (e.g. *“Book a Table”* or *“Confirm Reservation”*). Its modern yet neutral tone supports a professional restaurant brand while remaining visually appealing and consistent across browsers and devices (Google Fonts, 2024; 99designs, 2024; DesigningIt, 2024).

### Secondary Typeface – Lato (Body Text)

The humanist sans-serif typeface **Lato** is used for body text, menu descriptions, form labels, confirmation messages, and supporting informational content (Google Fonts, 2024; 99designs, 2024; Interaction Design Foundation, 2023).

**Justification:**  
Lato’s open letterforms and soft curves enhance readability, particularly at smaller sizes and on mobile devices. This makes it well suited for longer text blocks such as menu items, reservation details, and explanatory copy. Its friendly and approachable character complements the hospitality-focused nature of the website, helping users feel comfortable and confident when entering personal information or completing bookings (Google Fonts, 2024; 99designs, 2024; Interaction Design Foundation, 2023).

### Implementation

To ensure consistency, performance, and maintainability, only two typefaces are used across the website:

- **Montserrat** – for headings, navigation, key labels, and call-to-action buttons  
- **Lato** – for body text, paragraphs, form inputs, menus, and supporting content  

This restrained typographic approach improves visual coherence and reduces cognitive load for users.

### Typography Specifications

- **Body text minimum size:** `16px` (in line with accessibility and readability guidelines)
- **Font weights:**  
  - `400` for body content  
  - `600–700` for headings and call-to-action buttons  
- **System fallback stack:** `'Arial', sans-serif`  

These specifications ensure compliance with accessibility standards while maintaining a polished and professional visual presentation across all devices and screen sizes.

---

## References

[⬆ Back to Table of contents](#table-of-contents)

- **Code Institute (2025).** Data Centric Development – Milestone Project 3 Specification.
Dublin: Code Institute. Available at: https://learn.codeinstitute.net
  (Accessed: 27 December 2025).

- **W3C – World Wide Web Consortium (2023).** Web Content Accessibility Guidelines (WCAG) 2.2.
Available at: https://www.w3.org/WAI/standards-guidelines/wcag/
  (Accessed: 27 December 2025).

- **W3C (2023) Web Content Accessibility Guidelines (WCAG) 2.1.**
Available at: https://www.w3.org/TR/WCAG21/
  (Accessed: 11 January 2026).

- **Mozilla Developer Network (MDN) (2024).** HTML, CSS and Web Development Documentation.
Available at: https://developer.mozilla.org/
  (Accessed: 27 December 2025).

- **Mozilla Developer Network (2024).** JavaScript Guide and Progressive Enhancement.  
Available at: https://developer.mozilla.org/en-US/docs/Web/JavaScript  
  (Accessed: 29 December 2025).

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

- **Mozilla Developer Network (2024).** DOM Manipulation and Cross-Browser Compatibility.  
Available at: https://developer.mozilla.org/en-US/docs/Web  
  (Accessed: 29 December 2025).

- **Mozilla Developer Network (2024).** Testing JavaScript Applications.  
Available at: https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing  
  (Accessed: 29 December 2025).

- **Interaction Design Foundation (2023).** User-Centred Design and Usability Principles.
Available at: https://www.interaction-design.org/
  (Accessed: 27 December 2025).

- **Interaction Design Foundation (2023)** Color theory for designers.
Available at: https://www.interaction-design.org/literature/topics/color-theory
  (Accessed: 11 January 2026).

- **Interaction Design Foundation (2023)** Typography for user interfaces.
Available at: https://www.interaction-design.org/literature/topics/typography
  (Accessed: 11 January 2026).

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

- **Google Fonts (2024) Montserrat.**
Available at: https://fonts.google.com/specimen/Montserrat
  (Accessed: 11 January 2026).

- **Google Fonts (2024) Lato.**
Available at: https://fonts.google.com/specimen/Lato
  (Accessed: 11 January 2026).

- **Meta for Developers (2024).** Sharing Content on Facebook and Instagram. 
Available at: https://developers.facebook.com/docs/sharing/  
  (Accessed: 27 December 2025).

- **Meta Open Source (2024).** Jest Documentation.  
Available at: https://jestjs.io/docs/getting-started  
  (Accessed: 29 December 2025).

- **OpenWeather (2024).** OpenWeather API Documentation.
Available at: https://openweathermap.org/api  
  (Accessed: 27 December 2025).

- **X Developers (2024).** _X (formerly Twitter) Platform Developer Documentation._  
Available at: https://developer.x.com/  
  (Accessed: 27 December 2025).

- **JSHint (2024).** JavaScript Code Quality Tool. 
Available at: https://jshint.com/  
  (Accessed: 29 December 2025).

- **jQuery Foundation (2024).** jQuery API Documentation. 
Available at: https://api.jquery.com/  
  (Accessed: 29 December 2025).

- **Agrawal, S. (2025)** Color psychology in UX design: How colors influence user behavior.
Available at: https://www.uxdesign.cc/color-psychology-in-ux-design
  (Accessed: 11 January 2026).

- **Baradell, L. (2023)** The psychology of color in web design.
Available at: https://www.interaction-design.org/literature/article/the-psychology-of-color-in-web-design
  (Accessed: 11 January 2026).

- **Bootstrap (2024)** Bootstrap 5 documentation.
Available at: https://getbootstrap.com/docs/5.3/getting-started/introduction/
  (Accessed: 11 January 2026).

- **DesigningIt (2024)** Web color palettes and accessibility best practices.
Available at: https://designingit.com/web-design-color-palettes-accessibility
  (Accessed: 11 January 2026).

- **DesigningIt (2024)** Typography principles for modern web design.
Available at: https://designingit.com/typography-in-web-design
  (Accessed: 11 January 2026).

- **99designs (2024)** Typography in web design: Best practices and examples.
Available at: https://99designs.co.uk/blog/design-basics/web-typography/
  (Accessed: 11 January 2026).


