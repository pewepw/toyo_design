# TOYO TIRES ETEN - Order Management System Implementation Plan

## Project Overview
Implementation of comprehensive order management system for TOYO TIRES ETEN following the CSV requirements and flow diagram. The system includes dashboard, multiple order types, order management, and sales forecasting capabilities.

## Design System

### Colors
- **Primary**: #0062B0 (TOYO Blue)
- **Secondary**: #7F7F7F (TOYO Gray)
- **Light Gray**: #727272 (TOYO Light Gray)
- **Background**: #f0f0f0
- **Card Background**: #ffffff
- **Input Background**: #fafafa

### Typography
- **Font Family**: 'Helvetica Neue', sans-serif
- **Title**: 32px, font-weight: 700
- **Subtitle**: 16px, font-weight: 500
- **Body**: 14px, font-weight: 400
- **Button**: 16px, font-weight: 600

### Layout Specifications
- **Device Frame**: 393px × 852px (iPhone 16 Pro)
- **Border Radius**: 25px (device), 8px (buttons), 20px (cards)
- **Padding**: 15px (screen), 18px (buttons), 16px (inputs)
- **Status Bar Height**: 44px

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

### Module 2: Core Order Flow (8 screens)
**Files:**
- `2-place-order.html` - Order type selection (Clearance/Normal/Direct Shipment/Own Use)
- `2-1-credit-check.html` - Credit limit validation
- `2-2-ship-to-selection.html` - Ship-to location selection (Main Account only)
- `2-4-product-selection.html` - Product search and selection
- `2-4-1-normal-cart.html` - Shopping cart with delivery options
- `2-4-2-confirm-order.html` - Order confirmation
- `2-4-3-order-success.html` - Order creation success
- `2-4-4-back-order.html` - Back order handling

**Key Features:**
- Credit limit display without simulation delays
- Product search with filters (Pattern, Size, DOT, Origin)
- Stock status indicators with color coding
- Cart management with pickup/delivery options
- Static UI with no API simulation

### Module 3: Specialized Order Types (11 screens)

#### Clearance Orders (3 screens)
- `2-3-clearance-programs.html` - Clearance program selection
- `2-3-1-clearance-sku-list.html` - Clearance product listing with filters
- `2-3-2-clearance-cart.html` - Clearance cart management

#### Direct Shipment Orders (5 screens)
- `2-5-ds-cart-list.html` - Multiple DS cart management
- `2-5-1-ds-cart.html` - DS cart with truck sizing (20FT/40FT)
- `2-5-2-ds-product-selection.html` - DS product search
- `2-5-3-upload-product-list.html` - Excel template upload
- `2-5-4-ds-confirm-order.html` - DS order confirmation

#### Own Use Orders (3 screens)
- `2-6-own-use-products.html` - Own use product selection (2+2 requirement)
- `2-6-1-own-use-cart.html` - Own use cart (max 4 pcs, delivery only)
- `2-6-2-own-use-confirm.html` - Own use order confirmation

**Business Rules:**
- Clearance: Main account with ship-to selection
- Direct Shipment: 90% truck fill requirement, ETA D+2, 20FT for East Malaysia/Coast
- Own Use: Family Channel only, once yearly, minimum order 200k previous year, 2+2 tires

### Module 4: Order Management & Forecasting (8 screens)

#### Order Management (6 screens)
- `3-order-list.html` - Order listing with comprehensive filters
- `3-1-order-details.html` - Detailed order view with action buttons
- `3-1-1-order-receive-rate.html` - Delivery confirmation and rating (5-star)
- `3-1-2-reorder.html` - Reorder functionality from previous orders
- `3-2-return-request.html` - Return item selection (7 days from delivery)
- `3-2-1-return-confirmation.html` - Return confirmation with reasons

#### Sales Forecasting (2 screens)
- `4-1-generate-forecast.html` - Generate forecast template (last 6 months)
- `4-2-submit-forecast.html` - Upload and submit forecast data

**Business Rules:**
- Cancel: 30 minutes from order placement
- Return: 7 days from delivery date
- Back Order: Dealer cannot cancel
- Reorder: Based on previous order items

## Technical Implementation

### Framework & Libraries
- **HTML5** with semantic markup
- **TailwindCSS** via CDN for styling
- **FontAwesome** for icons
- **JavaScript** for interactions (no auto-redirects)

### Mobile-First Design
- iPhone 16 Pro dimensions (393×852px)
- iOS-style status bar with time, signal, battery
- Navigation guidelines: 
  - Bottom tab navigation only for main entry points (dashboard, index files)
  - Sub-screens with back buttons and header navigation do NOT need bottom nav
  - Only screens without top navigation headers require bottom navigation
- **Sticky Bottom Buttons**: 
  - Action buttons (Continue, Submit, Confirm, etc.) should be positioned fixed at bottom
  - Use `position: fixed` or `position: absolute` with `bottom: 0`
  - Add bottom padding to main content to prevent content from being hidden behind button
  - Ensure buttons remain visible and accessible regardless of scroll position
- Touch-friendly buttons and interactions

### UI Components (Static)
- Credit limit display cards
- Product listing with static data
- Ship-to location selection
- Order confirmation screens

### Data Management
- Product catalog with filters
- Shopping cart persistence
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
├── 2-4-1-normal-cart.html
├── 2-4-2-confirm-order.html
├── 2-4-3-order-success.html
├── 2-4-4-back-order.html
├── 2-5-ds-cart-list.html
├── 2-5-1-ds-cart.html
├── 2-5-2-ds-product-selection.html
├── 2-5-3-upload-product-list.html
├── 2-5-4-ds-confirm-order.html
├── 2-6-own-use-products.html
├── 2-6-1-own-use-cart.html
├── 2-6-2-own-use-confirm.html
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