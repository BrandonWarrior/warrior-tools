# Warrior Tools – Project Planning

## 🔍 Overview

**Warrior Tools** is an e-commerce web application designed for power tool enthusiasts, tradespeople, and DIYers. The platform allows users to browse, search, and purchase high-quality power tools. The goal of this application is to provide a fast, secure, and modern shopping experience with features such as account registration, product filtering, newsletter subscriptions, and an easy-to-use admin interface for managing products.

The application is being developed using the Django web framework and will include Stripe integration for secure payments, a relational database (initially SQLite, then PostgreSQL in production), and be fully deployed to a cloud hosting platform - Heroku

---

## 🎯 Objectives

- Build a fully functional, cloud-hosted Django e-commerce site
- Include full CRUD functionality for products
- Implement user registration, login, and email confirmation
- Create a responsive, UX-friendly interface using HTML/CSS/JS
- Integrate Stripe for secure checkout
- Add marketing features like a newsletter signup and social media links
- Follow SEO and accessibility best practices
- Manage the project using Agile principles and GitHub Projects

---

## Wireframes

A wireframe mockup of the Warrior Tools home page has been created using Balsamiq Wireframes, a tool used to quickly sketch out user interface layouts. These wireframes represent the planned structure and layout of the site’s main landing experience and guide the front-end development process.

![home page wireframe](docs/home-page-wf.png)
![home page wwireframe 2](docs/home-page-wf2.png)

### Layout Overview
- Header Section
Includes a clear logo and brand title “Warrior Tools”

A horizontal navigation menu provides links to:

Products, Profile, Sign In, Sign Up, and Sign Out

Adjusts dynamically depending on the user's authentication state

- Newsletter Signup
Centrally placed section encouraging users to subscribe to updates

Forms a key part of the marketing strategy by capturing visitor interest early

- Featured Products Section
A structured product grid displays six featured tools

Each product box will showcase a tool image and basic info

Supports user stories related to browsing and shopping

- Footer
A simple footer area is included for contact info, legal links, or additional navigation

---
## 📋 User Stories (Grouped by Epics)

### 🏷 Epic: Browsing and Shopping

- **Browse Tools by Category**  
  As a shopper, I want to browse power tools by category, so that I can easily find the right tools for my needs.

- **View Detailed Product Information**  
  As a shopper, I want to view detailed product information, so that I can decide whether it suits my requirements.

- **See Current Deals and Offers**  
  As a shopper, I want to see current deals and special offers, so that I can take advantage of any savings.

- **View Basket Total While Shopping**  
  As a shopper, I want to see the running total of my shopping basket, so that I can stay within my budget.

- **Search for Products**  
  As a shopper, I want to search for products by name or model, so that I can find specific tools quickly.

- **Filter Products by Criteria**  
  As a shopper, I want to filter results by brand, price, or rating, so that I can find the best tools for my needs.

---

### 🏷 Epic: User Accounts

- **Register for a Customer Account**  
  As a new user, I want to create an account, so that I can place orders and track my purchases.

- **Log In and Access My Account**  
  As a returning user, I want to log in securely, so that I can access my personal account.

- **Reset Forgotten Password**  
  As a user, I want to reset my password if I forget it, so that I can regain access without assistance.

- **Receive Registration Confirmation**  
  As a new user, I want to receive an email confirmation after registering, so that I know my account has been created successfully.

---

### 🏷 Epic: Newsletter and Marketing

- **Sign Up for the Newsletter**  
  As a visitor, I want to sign up for the Warrior Tools newsletter, so that I can receive updates, offers and tool tips.

- **Collect Newsletter Subscribers**  
  As the store owner, I want to collect email addresses via a newsletter form, so that I can grow a mailing list and promote products.

---

### 🏷 Epic: Checkout

- **Select Product Quantity and Options**  
  As a shopper, I want to select product quantity and size (if relevant), so that I can buy the correct items.

- **Enter Secure Payment Details**  
  As a shopper, I want to securely enter my payment details, so that I can complete my purchase with confidence.

- **Receive Order Confirmation Email**  
  As a customer, I want to receive an email confirmation after checking out, so that I have a record of my order.

---

### 🏷 Epic: Admin Product Management

- **Add New Products as Admin**  
  As the store owner, I want to add new products to the store, so that shoppers can purchase the latest tools.

- **Edit Existing Product Listings**  
  As the store owner, I want to edit existing product listings, so that information is accurate and up to date.

- **Remove Discontinued Products**  
  As the store owner, I want to remove discontinued products, so that customers don’t attempt to buy unavailable items.

---