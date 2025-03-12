# **RideShare - Software Requirements Specification (SRS)**  
**Version 1.0 - Approved**  
**Prepared by:**  
Gary Singh, Bek Salimov, Nathan Yung, Aryana Villafuerte, Bobby Hayes, and Christian White  
**Course:** UW Bothell CSS 360  
**Date:** 02/14/2025  

---

## 📌 **Table of Contents**  
1. [Introduction](#introduction)  
   - [Purpose](#purpose)  
   - [Document Conventions](#document-conventions)  
   - [Intended Audience and Reading Suggestions](#intended-audience-and-reading-suggestions)  
   - [Product Scope](#product-scope)  
   - [References](#references)  
2. [Overall Description](#overall-description)  
   - [Product Perspective](#product-perspective)  
   - [Product Functions](#product-functions)  
   - [User Classes and Characteristics](#user-classes-and-characteristics)  
   - [Operating Environment](#operating-environment)  
   - [Design and Implementation Constraints](#design-and-implementation-constraints)  
   - [User Documentation](#user-documentation)  
   - [Assumptions and Dependencies](#assumptions-and-dependencies)  
3. [External Interface Requirements](#external-interface-requirements)  
4. [System Features](#system-features)  
5. [Other Nonfunctional Requirements](#other-nonfunctional-requirements)  
6. [Other Requirements](#other-requirements)  

---

## 🔹 **Introduction**  
### **Purpose**  
This document outlines the functional and nonfunctional requirements for **RideShare**. The primary objective is to develop a platform where users can request rides and drivers can accept them. This SRS is intended for **developers, testers, and stakeholders** to understand system requirements and implementation details.

### **Document Conventions**  
- **Bolded words** indicate section headings and important keywords.  
- Requirements are assigned **priority levels** based on importance.  
- **TBD (To Be Determined)** is used for pending information.  

### **Intended Audience and Reading Suggestions**  
- **Developers:** Focus on **System Features** and **External Interfaces**.  
- **Users:** Review the **Product Scope** section for app functionality.  
- **Testers:** Examine **Functional & Nonfunctional Requirements** to verify compliance.  
- **Documentation Writers:** Follow **Document Conventions** and update accordingly.  

### **Product Scope**  
RideShare is a **web-based application** that allows users to **request rides from drivers**.  
- **Passengers:** Book rides, track drivers, and pay online.  
- **Drivers:** Accept rides, navigate to pickup points, and receive payments.  
- **Benefits:** Affordable transport for passengers and income opportunities for drivers.  
- **Key Features:** Ride matching, real-time tracking, and payment integration.  

### **References**  
TBD  

---

## 🔹 **Overall Description**  
### **Product Perspective**  
RideShare is a **standalone web application** designed for **convenient transportation**. Users can **request rides anywhere** within the supported geographic area.

### **Product Functions**  
- **User Management:** Account creation, login, and profile updates.  
- **Ride Booking:** Passengers request rides, drivers accept them.  
- **Payment Processing:** Secure transactions via third-party payment gateways.  
- **Location Sharing:** Real-time tracking of drivers and passengers.  

### **User Classes and Characteristics**  
| **User Type**  | **Role & Characteristics** |
|---------------|---------------------------|
| **Passengers** | Request rides, set destinations, and make payments. |
| **Drivers** | Accept rides, navigate to passengers, and receive payments. |
| **Developers** | Maintain system infrastructure and implement new features. |
| **Testers** | Verify the system’s functionality, security, and performance. |

### **Operating Environment**  
The application will be accessible via **desktop and mobile browsers** including:  
- **Google Chrome** (Version 133)  
- **Microsoft Edge** (Version 133)  
- **iOS Safari** (Version 18.3)  
- **Samsung Internet** (Version 27.07.17)  
- **Firefox** (Version 135)  

### **Design and Implementation Constraints**  
- **Limited to a specific geographic area** (Washington State).  
- **Third-party integrations** (Google Maps for navigation, Stripe for payments).  
- **Performance Constraints:** Optimized for devices with low processing power.  

### **User Documentation**  
- **Passenger Manual:** How to create an account, book rides, and make payments.  
- **Driver Manual:** Instructions for accepting rides, navigation, and earnings tracking.  

### **Assumptions and Dependencies**  
- Users must have **internet access** for real-time ride tracking.  
- Third-party services like **Google Maps & Stripe** must be operational.  
- The app must comply with **local transportation regulations**.  

---

## 🔹 **External Interface Requirements**  
### **User Interface**  
- **Simple and responsive UI** for passengers and drivers.  
- **Real-time ride tracking** using OpenStreetMap API.  

### **Hardware Interfaces**  
- **GPS-enabled browsers** for location tracking.  
- **Webcam support** (for driver verification).  

### **Software Interfaces**  
- **SQLite/PostgreSQL** for ride and user data storage.  
- **Google Maps API** for navigation.  
- **Stripe API** for payment processing.  

### **Communication Interfaces**  
- **Secure HTTPS connections** for all transactions.  
- **Push notifications** for ride status updates.  

---

## 🔹 **System Features**  
### **1. User Accounts**  
- **Passengers & Drivers** must register before using the system.  
- **Users must log in** before booking or accepting rides.  

### **2. Ride Request & Matching**  
- **Passengers request rides** by setting pickup & drop-off locations.  
- **System finds the nearest available driver** and assigns the ride.  

### **3. Ride Tracking**  
- **Passengers see driver location** in real time.  
- **Status updates** sent when driver is near pickup location.  

### **4. Payment Processing**  
- **Stripe API integration** for secure payments.  
- **Automatic fare calculation** based on distance & time.  

---

## 🔹 **Other Nonfunctional Requirements**  
### **Performance Requirements**  
- Support **100+ simultaneous users** without performance degradation.  
- Payments must process within **5 seconds**.  

### **Safety & Security Requirements**  
- **Drivers must verify identity** via facial recognition.  
- **All user data is encrypted** and secured with HTTPS.  
- **Only authorized users** can access ride & payment data.  

### **Software Quality Attributes**  
- **Usability:** Simple UI for all users.  
- **Scalability:** Backend designed to support future expansion.  
- **Maintainability:** Modular design for easy updates.  

---

## 🔹 **Scaling Considerations**  
### **Challenges for 10M+ Users**  
- A **single database** may struggle with high traffic.  
- Lack of **caching (Redis)** could slow response times.  
- No **load balancing** means server overload is possible.  

### **Scalability Solutions**  
- Implement **database sharding & clustering**.  
- Introduce **Redis caching** for fast user session retrieval.  
- Deploy **load balancers** to distribute traffic efficiently.  
- Transition from **monolithic** to **microservices architecture** for better flexibility.  

---

## 🔹 **To Be Determined (TBD) List**  
| **Item**  | **Explanation** |
|-----------|---------------|
| **Ride Fare Calculation** | Will pricing include surge pricing? |
| **Driver Ratings** | Will passengers be able to rate drivers? |
| **Refund Policy** | How will refunds be handled? |

---

## **📌 Final Notes**  
RideShare aims to provide a **reliable, secure, and scalable** ridesharing platform. The current MVP focuses on **core ride-matching and payment functionalities**, with future iterations improving **security, scalability, and driver management**.  

🚀 **Stay tuned for updates!**  
