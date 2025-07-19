# TOYO TIRES ETEN - Order Management System Implementation Plan

## Project Overview
Implementation of comprehensive order management system for TOYO TIRES ETEN following the CSV requirements and flow diagram. The system includes dashboard, multiple order types, order management, and sales forecasting capabilities.

## Design System

Refer to **[Design System Specification](design-spec.md)** for comprehensive UI guidelines, component library, and navigation patterns.

## Module Implementation Strategy

### Module 1: Dashboard & Foundation
**Files:**
- `1-dashboard.html` - Main dashboard screen
- `index-order.html` - Showcase file

**Features:**
- Sales Target (Family Channel Only)
- Available Credit Limit
- Processing Orders count
- Processing Claims count
- Last 3 months warranty registered
- Campaign information

### Module 2: Core Order Flow (21 screens)
**Files:**
- `2-place-order.html` - Order type selection (Clearance/Normal/Direct Shipment/Own Use)
- `2-1-credit-check.html` - Credit limit validation
- `2-2-ship-to-selection.html` - Ship-to location selection (Main Account only)
- `2-3-clearance-programs.html` - Clearance program selection
- `2-3-1-clearance-sku-list.html` - Clearance product listing with filters
- `2-3-2-clearance-cart.html` - Clearance cart management
- `2-4-product-selection.html` - Product search and selection (Normal Order)
- **Note**: 2.4.1 "Get Price & Stock" is an SAP API function (no UI screen required)
- `2-4-2-normal-cart.html` - Shopping cart with delivery options
- `2-4-3-confirm-order.html` - Order confirmation
- `2-4-4-order-success.html` - Order creation success
- `2-4-5-back-order.html` - Back order handling
- `2-5-ds-cart-list.html` - Multiple DS cart management
- `2-5-1-ds-cart.html` - DS cart with truck sizing (20FT/40FT)
- `2-5-2-ds-product-selection.html` - DS product search
- `2-5-3-upload-product-list.html` - Excel template upload
- `2-5-4-ds-confirm-order.html` - DS order confirmation
- `2-5-5-create-ds-order.html` - DS order creation
- `2-6-own-use-products.html` - Own use product selection (2+2 requirement)
- `2-6-1-own-use-cart.html` - Own use cart (max 4 pcs, delivery only)
- `2-6-2-own-use-confirm.html` - Own use order confirmation
- `2-6-3-create-own-use-order.html` - Own use order creation

**Key Features:**
- Credit limit display and validation
- Ship-to location selection for Main Accounts
- Clearance program selection and product listing
- Product search with filters (Pattern, Size, DOT, Origin)
- Stock status indicators with color coding
- Cart management with pickup/delivery options
- Direct Shipment cart management with truck sizing
- Own Use order restrictions and business rules
- Order confirmation and creation flows
- Back order handling for stock shortages
- Static UI with no API simulation

### Module 3: Order Management (6 screens)
**Files:**
- `3-order-list.html` - Order listing with comprehensive filters
- `3-1-order-details.html` - Detailed order view with action buttons
- `3-1-1-order-receive-rate.html` - Delivery confirmation and rating (5-star)
- `3-1-2-reorder.html` - Reorder functionality from previous orders
- `3-2-return-request.html` - Return item selection (7 days from delivery)
- `3-2-1-return-confirmation.html` - Return confirmation with reasons

**Business Rules:**
- Cancel: 30 minutes from order placement
- Return: 7 days from delivery date
- Back Order: Dealer cannot cancel
- Reorder: Based on previous order items

### Module 4: Sales Forecasting (2 screens)
**Files:**
- `4-1-generate-forecast.html` - Generate forecast template (last 6 months)
- `4-2-submit-forecast.html` - Upload and submit forecast data

**Business Rules:**
- Forecast based on last 6 months order history
- Excel template download and upload functionality
- Dealer value updates and submissions

## Technical Implementation

### Framework & Libraries
- **HTML5** with semantic markup
- **TailwindCSS** via CDN for styling
- **FontAwesome** for icons
- **JavaScript** for interactions (no auto-redirects)
- **Design System**: Follow [design-spec.md](design-spec.md) for all UI components

### Static UI Components
- Credit limit display cards
- Product listing with static data
- Ship-to location selection
- Order confirmation screens

### Data Management (Static)
- Product catalog with filters
- Shopping cart persistence simulation
- Order history tracking
- User preferences

## File Structure
```
design-5/order/
├── index-order.html (Main showcase)
├── 1-dashboard.html
├── 2-place-order.html
├── 2-1-credit-check.html
├── 2-2-ship-to-selection.html
├── 2-3-clearance-programs.html
├── 2-3-1-clearance-sku-list.html
├── 2-3-2-clearance-cart.html
├── 2-4-product-selection.html
├── 2-4-2-normal-cart.html
├── 2-4-3-confirm-order.html
├── 2-4-4-order-success.html
├── 2-4-5-back-order.html
├── 2-5-ds-cart-list.html
├── 2-5-1-ds-cart.html
├── 2-5-2-ds-product-selection.html
├── 2-5-3-upload-product-list.html
├── 2-5-4-ds-confirm-order.html
├── 2-5-5-create-ds-order.html
├── 2-6-own-use-products.html
├── 2-6-1-own-use-cart.html
├── 2-6-2-own-use-confirm.html
├── 2-6-3-create-own-use-order.html
├── 3-order-list.html
├── 3-1-order-details.html
├── 3-1-1-order-receive-rate.html
├── 3-1-2-reorder.html
├── 3-2-return-request.html
├── 3-2-1-return-confirmation.html
├── 4-1-generate-forecast.html
└── 4-2-submit-forecast.html
```

## Quality Standards
- **Accessibility**: WCAG 2.1 AA compliance
- **Performance**: Fast loading, smooth interactions
- **Consistency**: Uniform design patterns across all screens
- **Validation**: Client-side form validation
- **Error Handling**: User-friendly error messages
- **Documentation**: Inline code comments for complex logic

## Testing Checklist
- [ ] Cross-browser compatibility (Safari, Chrome, Firefox)
- [ ] Mobile responsiveness on various devices
- [ ] Touch interactions and gestures
- [ ] Form validation and error states
- [ ] Navigation flow between screens
- [ ] Business rule implementations
- [ ] API integration mockups
- [ ] Performance optimization

## Deployment
Files will be integrated into the main `design-5/index.html` showcase upon completion of all modules.