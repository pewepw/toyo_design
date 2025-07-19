# ETEN Warranty System - Implementation Plan

## Project Overview
Implementation of a comprehensive warranty management system for TOYO TIRES ETEN application, consisting of 25+ mobile screens following iOS design guidelines and existing design patterns.

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

## Screen Specifications

### 1. Claim Appointment Dashboard
**File**: `warranty/1-claim-appointment.html`
**Purpose**: Main dashboard for claim management
**Components**:
- Custom bottom navigation bar
- 3 summary cards: Requests, Scheduled Appointments, Pending Claims
- Action buttons: View Requests, Schedule Appointments
- Status indicators with numbers

### 1.1 Appointment Request List
**File**: `warranty/1-1-appointment-request.html`
**Purpose**: List of incoming claim appointment requests
**Components**:
- Header with back button and title
- List of request cards showing:
  - Application Date
  - Preferred Appointment Date/Time
  - Customer Name
  - Mobile Number
- Tap to view details functionality

### 1.1.1 Claim Details (Request)
**File**: `warranty/1-1-1-claim-details.html`
**Purpose**: Detailed view of claim request
**Components**:
- Customer information section
- Tire details (Pattern, Size, Serial Plate)
- Warranty Certificate Number
- Problem description
- 3 submitted photos in gallery
- Accept/Reject action buttons

### 1.1.2 Accept and Notify
**File**: `warranty/1-1-2-accept-notify.html`
**Purpose**: Schedule confirmation for accepted appointment
**Components**:
- Date picker component
- Time slot selection
- Confirm and Notify button
- Customer notification preview

### 1.1.3 Appointment Accepted
**File**: `warranty/1-1-3-appointment-accepted.html`
**Purpose**: Confirmation screen after acceptance
**Components**:
- Success message with checkmark icon
- Appointment details summary
- Done button
- Create Order button (optional action)

### 1.1.4 Reject Reason Selection
**File**: `warranty/1-1-4-reject-reason.html`
**Purpose**: Reason selection for appointment rejection
**Components**:
- Radio button list of preset reasons
- Custom reason text input option
- Confirm Reject button
- Cancel option

### 1.1.5 Appointment Rejected
**File**: `warranty/1-1-5-appointment-rejected.html`
**Purpose**: Confirmation of rejection with customer notification
**Components**:
- Rejection confirmation message
- Selected reason display
- Customer notification status
- Done button

### 1.2 Schedule Appointment List
**File**: `warranty/1-2-schedule-appointment.html`
**Purpose**: List of upcoming scheduled appointments
**Components**:
- Date/time sorted list
- Customer information cards
- Scan QR Code button for each appointment
- Status indicators

### 1.2.1 Scan Claim QR Code
**File**: `warranty/1-2-1-scan-qr-code.html`
**Purpose**: Camera interface for QR code scanning
**Components**:
- Camera viewfinder simulation
- QR code detection overlay
- Instructions text
- Manual entry fallback option

### 1.2.2 Claim Details (Scanned)
**File**: `warranty/1-2-2-claim-details.html`
**Purpose**: Display claim details from scanned QR
**Components**:
- All claim information sections
- Read-only view of customer data
- Tire and warranty details
- Submitted photos
- Next button to proceed

### 1.2.3 Claim Check List
**File**: `warranty/1-2-3-claim-checklist.html`
**Purpose**: 10-point verification checklist
**Components**:
- 10 checkboxes with inspection points
- Progressive enabling (all must be checked)
- Reject button (always available)
- Next button (enabled when all checked)
- Visual progress indicator

### 1.2.4 Upload Photo
**File**: `warranty/1-2-4-upload-photo.html`
**Purpose**: Photo upload for damaged tire documentation
**Components**:
- Tread Depth Photo upload slot
- 5 additional photo upload slots
- Camera/gallery selection
- Photo preview thumbnails
- Submit button

### 1.2.5 Claim Filed to Toyo
**File**: `warranty/1-2-5-claim-filed.html`
**Purpose**: Success message for filed claim
**Components**:
- Success icon and message
- Claim reference number
- Filed date/time
- Done button
- View Claim List option

### 1.2.6 Reject Reason (Checklist Failure)
**File**: `warranty/1-2-6-reject-reason.html`
**Purpose**: Rejection reasons for failed checklist
**Components**:
- Failed checklist items highlight
- Reason selection dropdown
- Additional notes text area
- Confirm Reject button

### 2. Claim List
**File**: `warranty/2-claim-list.html`
**Purpose**: List all filed claims with status tracking
**Components**:
- Search and filter options
- Claim cards showing:
  - Claim Date
  - Claim Number
  - Current Status
  - Action buttons
- Status color coding

### 2.1 Claim Details (Progress)
**File**: `warranty/2-1-claim-details.html`
**Purpose**: Detailed claim progress and actions
**Components**:
- Claim information header
- Progress timeline
- Current status indicator
- Action buttons based on status:
  - CTC Button
  - Scrap Upload
  - New Tire Receive
  - Show Report

### 2.1.1 Claim Report
**File**: `warranty/2-1-1-claim-report.html`
**Purpose**: Complete claim report display
**Components**:
- Full claim report layout
- PDF-style formatting
- All claim details and timeline
- Print/Share options
- Back to claim details

### 2.2 CTC (Call to Customer)
**File**: `warranty/2-2-ctc.html`
**Purpose**: CTC requirement and collection time display
**Components**:
- CTC status flag
- Collection instructions
- Contact information
- Time requirements
- Mark as completed button

### 2.3 Scrap Instructions
**File**: `warranty/2-3-scrap.html`
**Purpose**: Scrap procedure with photo upload
**Components**:
- Scrap guidelines text
- Required photo specifications
- Upload photo button
- Preview uploaded photos
- Submit button

### 2.3.1 Scrap Summary
**File**: `warranty/2-3-1-scrap-summary.html`
**Purpose**: Scrap upload confirmation
**Components**:
- Success message
- Uploaded photos confirmation
- Submission timestamp
- Done button

### 2.4 Reimbursement
**File**: `warranty/2-4-reimbursement.html`
**Purpose**: Invoice upload for reimbursement claims
**Components**:
- Reimbursement instructions
- Invoice upload area
- File format requirements
- Attach Invoice button
- Submit button

### 2.4.1 Invoice Submitted
**File**: `warranty/2-4-1-invoice-submitted.html`
**Purpose**: Invoice submission confirmation
**Components**:
- Success message
- Submission details
- Processing timeline
- Done button

### 2.5 Create Claim
**File**: `warranty/2-5-create-claim.html`
**Purpose**: Manual claim creation form
**Components**:
- Tire information form:
  - Pattern & Size dropdown
  - Serial Plate input
  - Warranty Certificate Number (optional)
  - Warranty Type selection
  - Vehicle Number (optional)
- Problem description
- Customer/Dealer information
- Next button to photo upload

## Navigation Structure

### Navigation Guidelines
- **Bottom Navigation**: Only for main entry points and dashboard screens
- **Sub-screens**: Use back buttons in top-left header, NO bottom navigation
- **Rule**: Screens with back buttons and header navigation do NOT need bottom nav
- **Only include bottom nav**: On screens without top navigation headers

### Sticky Bottom Buttons
- **Action buttons** (Continue, Submit, Confirm, Accept, Reject, etc.) should be positioned fixed at bottom
- Use `position: fixed` or `position: absolute` with `bottom: 0`
- Add bottom padding to main content to prevent content from being hidden behind button
- Ensure buttons remain visible and accessible regardless of scroll position
- Button container should have background and padding for better UX

### Custom Bottom Navigation (When Applicable)
Based on the provided design, implement a rounded blue navigation bar with 5 icons:
1. Home (selected state)
2. Shopping/Orders
3. Search
4. Claims/Warranty
5. Profile

### Navigation Patterns
- Back button in top-left for sub-screens
- Breadcrumb navigation for deep flows
- Tab switching for related content
- Modal overlays for confirmations

## Technical Implementation

### Base Template Structure
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ETEN - [Screen Name]</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <!-- Custom styles -->
</head>
<body>
    <div class="device-frame">
        <div class="screen-content">
            <!-- Status Bar -->
            <!-- Main Content -->
            <!-- Bottom Navigation -->
        </div>
    </div>
</body>
</html>
```

### Shared Components
- Status bar with time and battery
- Navigation headers with back buttons
- Form inputs with icons
- Button styles (primary, secondary, danger)
- Card layouts
- Photo upload components
- Modal overlays

### Interactive Elements
- Form validation
- Photo upload UI (static mockups)
- QR code scanner UI (static interface)
- Date/time picker UI
- Checkbox interactions
- Button state management (no API calls)

## File Organization
```
design-5/
├── warranty/
│   ├── [25+ HTML files as specified]
├── images/
│   ├── toyo-tires.png
│   ├── ETEN.png
│   └── [additional assets]
└── specs/
    └── implementation-plan.md
```

## Quality Assurance
- Responsive design testing
- Cross-browser compatibility
- Accessibility compliance
- Performance optimization
- Code consistency
- Design system adherence