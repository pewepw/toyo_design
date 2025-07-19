# TOYO TIRES ETEN - Design System Specification

## Overview
Comprehensive design system for TOYO TIRES ETEN application, providing consistent UI patterns, components, and guidelines for mobile-first prototype development following iOS Human Interface Guidelines.

## Brand Identity

### Colors
- **Primary**: #0062B0 (TOYO Blue)
- **Secondary**: #7F7F7F (TOYO Gray)  
- **Light Gray**: #727272 (TOYO Light Gray)
- **Background**: #f0f0f0
- **Card Background**: #ffffff
- **Input Background**: #fafafa
- **Success**: #28a745
- **Warning**: #ffa726
- **Error**: #dc3545
- **Info**: #17a2b8

### Typography
- **Font Family**: 'Helvetica Neue', sans-serif
- **Title**: 32px, font-weight: 700
- **Header**: 28px, font-weight: 700
- **Section Title**: 20px, font-weight: 600
- **Subtitle**: 18px, font-weight: 600
- **Body Large**: 16px, font-weight: 500
- **Body**: 14px, font-weight: 400
- **Caption**: 12px, font-weight: 500
- **Button**: 16px, font-weight: 600

### Brand Assets
- **Logo**: `../images/toyo-tires.png` (primary brand logo)
- **Logo White**: `../images/toyo-tires-white.png` (white version)
- **ETEN Logo**: `../images/ETEN.png` (application logo)

## Layout System

### Device Specifications (iPhone 16 Pro)
- **Screen Dimensions**: 393px × 852px
- **Device Frame**: 
  - Width: 393px
  - Height: 852px
  - Border Radius: 25px
  - Background: #000
  - Padding: 2px
  - Box Shadow: 0 8px 30px rgba(0,0,0,0.3)

### Screen Content Structure
- **Screen Content**: 
  - Border Radius: 23px
  - Background: white
  - Position: relative
  - Overflow: hidden

### Status Bar
- **Height**: 44px
- **Background**: white
- **Content**: Time (left), Signal/WiFi/Battery icons (right)
- **Typography**: 14px, font-weight: 600, color: #333

### Spacing & Measurements
- **Screen Padding**: 15px
- **Button Padding**: 18px
- **Input Padding**: 16px
- **Card Padding**: 20px
- **Border Radius**: 
  - Device: 25px
  - Cards: 20px
  - Buttons: 8px-12px
  - Inputs: 8px

## Navigation System

### Navigation Rules
1. **Bottom Navigation**: Only for main entry points (dashboard, index files)
2. **Top Header Navigation**: For sub-screens with back navigation
3. **Mutual Exclusivity**: Screens with top headers do NOT include bottom navigation
4. **Decision Logic**: Only screens without top navigation headers require bottom navigation

### Bottom Navigation Pattern
```css
.bottom-nav {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    height: 110px;
    background: transparent;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 30px 40px;
    z-index: 10;
}

.nav-container {
    background: #0062B0;
    border-radius: 30px;
    padding: 12px 24px;
    display: flex;
    gap: 40px;
    box-shadow: 0 4px 20px rgba(0,98,176,0.3);
    width: 100%;
}

.nav-item {
    color: rgba(255,255,255,0.6);
    font-size: 20px;
    cursor: pointer;
    transition: all 0.2s ease;
    padding: 8px;
    border-radius: 12px;
}

.nav-item.active {
    color: white;
    background: rgba(255,255,255,0.2);
}

.nav-item:hover {
    color: white;
    transform: scale(1.1);
}
```

### Top Header Navigation Pattern
```css
.header {
    background: white;
    padding: 16px 15px;
    border-bottom: 1px solid #f0f0f0;
    display: flex;
    align-items: center;
    gap: 16px;
}

.back-button {
    width: 40px;
    height: 40px;
    border-radius: 12px;
    background: #f8f9fa;
    border: 1px solid #e9ecef;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #0062B0;
    font-size: 16px;
    cursor: pointer;
    transition: all 0.2s ease;
}

.back-button:hover {
    background: #0062B0;
    color: white;
    border-color: #0062B0;
}

.header-title {
    font-size: 20px;
    font-weight: 600;
    color: #333;
    flex: 1;
}
```

### Navigation HTML Templates

#### Bottom Navigation Template
```html
<!-- Bottom Navigation -->
<div class="bottom-nav">
    <div class="nav-container">
        <div class="nav-item active">
            <i class="fas fa-home"></i>
        </div>
        <div class="nav-item">
            <i class="fas fa-shopping-bag"></i>
        </div>
        <div class="nav-item">
            <i class="fas fa-search"></i>
        </div>
        <div class="nav-item">
            <i class="fas fa-user"></i>
        </div>
    </div>
</div>
```

#### Top Header Template
```html
<!-- Header -->
<div class="header">
    <button class="back-button" onclick="window.location.href='previous-screen.html'">
        <i class="fas fa-arrow-left"></i>
    </button>
    <h1 class="header-title">Screen Title</h1>
    <!-- Optional: Action button or badge on right -->
</div>
```

## Component Library

### Buttons

#### Primary Button
```css
.primary-button {
    background: #0062B0;
    color: white;
    padding: 16px 24px;
    border-radius: 12px;
    font-size: 16px;
    font-weight: 600;
    border: none;
    cursor: pointer;
    transition: all 0.2s ease;
    width: 100%;
}

.primary-button:hover {
    background: #004d8c;
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(0,98,176,0.3);
}
```

#### Secondary Button
```css
.secondary-button {
    background: transparent;
    color: #0062B0;
    padding: 16px 24px;
    border: 2px solid #0062B0;
    border-radius: 12px;
    font-size: 16px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s ease;
    width: 100%;
}

.secondary-button:hover {
    background: #0062B0;
    color: white;
}
```

#### Danger Button
```css
.danger-button {
    background: #dc3545;
    color: white;
    padding: 16px 24px;
    border-radius: 12px;
    font-size: 16px;
    font-weight: 600;
    border: none;
    cursor: pointer;
    transition: all 0.2s ease;
}

.danger-button:hover {
    background: #c82333;
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(220,53,69,0.3);
}
```

### Cards

#### Standard Card
```css
.card {
    background: white;
    border-radius: 20px;
    padding: 24px 20px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.08);
    border: 1px solid #f0f0f0;
    transition: all 0.2s ease;
}

.card:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 30px rgba(0,0,0,0.12);
}
```

#### Section Card
```css
.section-card {
    background: white;
    border-radius: 16px;
    padding: 20px;
    margin-bottom: 16px;
    box-shadow: 0 4px 16px rgba(0,0,0,0.08);
    border: 1px solid #f0f0f0;
}
```

### Form Elements

#### Input Fields
```css
.form-input {
    width: 100%;
    padding: 16px;
    background: #fafafa;
    border: 1px solid #e9ecef;
    border-radius: 8px;
    font-size: 16px;
    color: #333;
    transition: all 0.2s ease;
}

.form-input:focus {
    outline: none;
    border-color: #0062B0;
    background: white;
    box-shadow: 0 0 0 3px rgba(0,98,176,0.1);
}
```

#### Label
```css
.form-label {
    font-size: 14px;
    font-weight: 500;
    color: #333;
    margin-bottom: 8px;
    display: block;
}
```

### Content Spacing & Layout System

#### Critical: Content Spacing for Fixed Elements
To prevent content from being hidden behind floating/fixed elements, follow these spacing rules:

**Basic Rule**: Always add bottom padding to `.main-content` based on fixed elements present:

```css
/* For screens with sticky bottom buttons only */
.main-content {
    padding-bottom: 100px; /* 70px button height + 30px safe margin */
}

/* For screens with bottom navigation only */
.main-content {
    padding-bottom: 110px; /* Bottom nav height */
}

/* For screens with sticky buttons + bottom navigation */
.main-content {
    padding-bottom: 180px; /* 70px buttons + 110px nav */
}

/* For screens with header + sticky buttons */
.main-content {
    height: calc(100% - 44px - 73px - 80px); /* Status bar - Header - Button space */
    padding-bottom: 20px;
}

/* For complex layouts (header + search + stats + fixed buttons) */
.main-content {
    height: calc(100% - 44px - 73px - 65px - 100px); /* All fixed element heights */
    padding-bottom: 16px;
}
```

#### Height Calculation Guidelines

**Standard Heights:**
- Status Bar: `44px`
- Header: `73px` (16px padding top/bottom + 40px button + 1px border)
- Search Container: `65px` (16px padding + 32px input + 1px border)
- Bottom Navigation: `110px`
- Sticky Action Buttons: `80px` (16px + 48px + 16px)
- FAB Safe Space: `100px`

### Sticky Bottom Buttons

#### Fixed Bottom Actions
```css
.action-buttons {
    position: fixed;
    bottom: 30px;
    left: 15px;
    right: 15px;
    display: flex;
    gap: 12px;
    padding: 16px 2px;
    z-index: 10;
}

.action-button {
    flex: 1;
    padding: 16px;
    border-radius: 12px;
    font-size: 16px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s ease;
    border: none;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
}

/* Single button layout */
.single-action {
    padding: 18px;
    border-radius: 12px;
    font-size: 16px;
    font-weight: 600;
    width: 100%;
    box-shadow: 0 4px 20px rgba(0,98,176,0.3);
}
```

### Status Indicators

#### Badge
```css
.badge {
    padding: 4px 8px;
    border-radius: 8px;
    font-size: 12px;
    font-weight: 600;
    display: inline-block;
}

.badge-success { background: #d4edda; color: #155724; }
.badge-warning { background: #fff3cd; color: #856404; }
.badge-danger { background: #f8d7da; color: #721c24; }
.badge-info { background: #d1ecf1; color: #0c5460; }
```

### Icons

#### Icon Container
```css
.icon-container {
    width: 48px;
    height: 48px;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
    color: white;
}

.icon-primary { background: #0062B0; }
.icon-success { background: #28a745; }
.icon-warning { background: #ffa726; }
.icon-danger { background: #dc3545; }
.icon-info { background: #17a2b8; }
```

## Advanced Form Components

### Search Input
```css
.search-container {
    padding: 16px 15px;
    background: white;
    border-bottom: 1px solid #f0f0f0;
}

.search-box {
    position: relative;
}

.search-input {
    width: 100%;
    padding: 12px 16px 12px 48px;
    border: 1px solid #ddd;
    border-radius: 12px;
    font-size: 14px;
    background: #fafafa;
    color: #333;
    transition: all 0.2s ease;
}

.search-input:focus {
    outline: none;
    border-color: #0062B0;
    background-color: white;
    box-shadow: 0 0 0 3px rgba(0,98,176,0.1);
}

.search-icon {
    position: absolute;
    left: 16px;
    top: 50%;
    transform: translateY(-50%);
    color: #999;
    font-size: 16px;
}
```

### Checklist Components
```css
.checklist-item {
    display: flex;
    align-items: flex-start;
    gap: 12px;
    padding: 16px;
    border: 1px solid #e0e0e0;
    border-radius: 12px;
    cursor: pointer;
    transition: all 0.2s ease;
    background: #fafafa;
}

.checklist-item:hover {
    border-color: #0062B0;
    background: #f0f9ff;
}

.checklist-item.checked {
    border-color: #4CAF50;
    background: #e8f5e8;
}

.checkbox {
    width: 24px;
    height: 24px;
    border: 2px solid #ddd;
    border-radius: 6px;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.2s ease;
    flex-shrink: 0;
    margin-top: 2px;
}

.checklist-item.checked .checkbox {
    border-color: #4CAF50;
    background: #4CAF50;
}

.checkbox i {
    color: white;
    font-size: 14px;
    opacity: 0;
    transition: opacity 0.2s ease;
}

.checklist-item.checked .checkbox i {
    opacity: 1;
}
```

### Photo Upload Components
```css
.upload-box {
    border: 2px dashed #ddd;
    border-radius: 12px;
    padding: 40px 20px;
    text-align: center;
    cursor: pointer;
    transition: all 0.2s ease;
    background: #fafafa;
    position: relative;
    overflow: hidden;
}

.upload-box:hover {
    border-color: #0062B0;
    background: #f0f9ff;
}

.upload-box.has-photo {
    padding: 0;
    border: 1px solid #ddd;
    background: none;
}

.photo-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
}

.photo-slot {
    aspect-ratio: 1;
    border: 2px dashed #ddd;
    border-radius: 12px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: all 0.2s ease;
    background: #fafafa;
    position: relative;
    overflow: hidden;
}

.photo-slot:hover {
    border-color: #0062B0;
    background: #f0f9ff;
}

.photo-overlay {
    position: absolute;
    top: 8px;
    right: 8px;
    display: flex;
    gap: 4px;
}

.photo-action {
    width: 32px;
    height: 32px;
    border-radius: 16px;
    background: rgba(0,0,0,0.7);
    color: white;
    border: none;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: all 0.2s ease;
}

.photo-action:hover {
    background: rgba(0,98,176,0.8);
}
```

### Progress Indicators
```css
.progress-container {
    background: #f8f9fa;
    border-radius: 20px;
    padding: 3px;
    margin-bottom: 12px;
}

.progress-bar {
    height: 8px;
    background: #0062B0;
    border-radius: 20px;
    width: 0%;
    transition: width 0.3s ease;
}

.progress-badge {
    padding: 4px 8px;
    border-radius: 8px;
    font-size: 12px;
    font-weight: 600;
    background: #f0f9ff;
    color: #0062B0;
    display: flex;
    align-items: center;
    gap: 4px;
}
```

### Required Field Indicators
```css
.required-label {
    background: #dc3545;
    color: white;
    font-size: 10px;
    font-weight: 600;
    padding: 2px 6px;
    border-radius: 4px;
    margin-left: 8px;
    text-transform: uppercase;
}

.form-group.required .form-label::after {
    content: ' *';
    color: #dc3545;
    font-weight: 700;
}
```

## Advanced Card & List Patterns

### Complex Cards
```css
.claim-card {
    background: white;
    border-radius: 16px;
    padding: 20px;
    box-shadow: 0 4px 16px rgba(0,0,0,0.08);
    border: 1px solid #f0f0f0;
    cursor: pointer;
    transition: all 0.2s ease;
}

.claim-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(0,0,0,0.12);
}

.card-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 12px;
}

.card-actions {
    display: flex;
    gap: 8px;
    margin-top: 16px;
}

.action-btn {
    padding: 8px 12px;
    border-radius: 8px;
    font-size: 12px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s ease;
    border: none;
    display: flex;
    align-items: center;
    gap: 4px;
}

.btn-primary {
    background: #0062B0;
    color: white;
}

.btn-primary:hover {
    background: #004d8c;
}

.btn-secondary {
    background: #f8f9fa;
    color: #666;
    border: 1px solid #e9ecef;
}

.btn-secondary:hover {
    background: #e9ecef;
    color: #333;
}
```

### Stats Grid Layouts
```css
/* 4-column stats grid */
.stats-summary {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 12px;
    margin-bottom: 20px;
}

.stat-card {
    background: white;
    border-radius: 12px;
    padding: 16px 12px;
    text-align: center;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    border: 1px solid #f0f0f0;
}

.stat-number {
    font-size: 20px;
    font-weight: 700;
    color: #333;
    margin-bottom: 4px;
}

.stat-label {
    font-size: 11px;
    color: #666;
    font-weight: 500;
}

/* Status-specific colors */
.stat-card.pending .stat-number { color: #f39c12; }
.stat-card.in-progress .stat-number { color: #3498db; }
.stat-card.completed .stat-number { color: #27ae60; }
.stat-card.rejected .stat-number { color: #e74c3c; }
```

## Status & Feedback Components

### Status Badges
```css
.status-badge {
    padding: 4px 8px;
    border-radius: 6px;
    font-size: 12px;
    font-weight: 600;
    text-transform: uppercase;
    display: inline-block;
}

.status-pending {
    background: #fff3cd;
    color: #856404;
}

.status-in-progress {
    background: #d1ecf1;
    color: #0c5460;
}

.status-completed {
    background: #d4edda;
    color: #155724;
}

.status-rejected {
    background: #f8d7da;
    color: #721c24;
}

.status-urgent {
    background: #fee;
    color: #d32f2f;
}
```

### Info Boxes & Guidelines
```css
.info-box {
    background: #f0f9ff;
    border: 1px solid #0062B0;
    border-radius: 12px;
    padding: 16px;
    margin-bottom: 20px;
}

.info-title {
    font-size: 14px;
    font-weight: 600;
    color: #0062B0;
    margin-bottom: 8px;
    display: flex;
    align-items: center;
    gap: 8px;
}

.instruction-list {
    list-style: none;
    padding: 0;
    margin: 0;
}

.instruction-list li {
    font-size: 13px;
    color: #333;
    margin-bottom: 4px;
    padding-left: 16px;
    position: relative;
}

.instruction-list li::before {
    content: '•';
    color: #0062B0;
    position: absolute;
    left: 0;
}
```

### Empty States
```css
.empty-state {
    text-align: center;
    padding: 40px 20px;
    color: #666;
}

.empty-state i {
    font-size: 48px;
    margin-bottom: 16px;
    color: #ddd;
}

.empty-state h3 {
    font-size: 18px;
    margin-bottom: 8px;
    color: #999;
    font-weight: 600;
}

.empty-state p {
    font-size: 14px;
    line-height: 1.4;
    color: #666;
}
```

### Counter Badges
```css
.counter-badge {
    padding: 4px 8px;
    border-radius: 8px;
    font-size: 12px;
    font-weight: 600;
    background: #f0f9ff;
    color: #0062B0;
    display: inline-block;
}

.photo-count {
    padding: 4px 8px;
    border-radius: 8px;
    font-size: 12px;
    font-weight: 600;
    background: #f0f9ff;
    color: #0062B0;
}
```

## Floating & Fixed Elements

### Floating Action Button (FAB)
```css
.fab {
    position: fixed;
    bottom: 30px;
    right: 30px;
    width: 60px;
    height: 60px;
    border-radius: 50%;
    background: #0062B0;
    color: white;
    border: none;
    font-size: 24px;
    cursor: pointer;
    transition: all 0.2s ease;
    box-shadow: 0 6px 20px rgba(0,98,176,0.3);
    z-index: 1000;
}

.fab:hover {
    background: #004d8c;
    transform: scale(1.1);
    box-shadow: 0 8px 24px rgba(0,98,176,0.4);
}

/* Mini FAB */
.fab-mini {
    width: 48px;
    height: 48px;
    font-size: 20px;
}
```

### Header Actions
```css
.header-actions {
    display: flex;
    gap: 8px;
}

.filter-button {
    width: 40px;
    height: 40px;
    border-radius: 12px;
    background: #f8f9fa;
    border: 1px solid #e9ecef;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #0062B0;
    font-size: 16px;
    cursor: pointer;
    transition: all 0.2s ease;
}

.filter-button:hover {
    background: #0062B0;
    color: white;
    border-color: #0062B0;
}
```

## Interactive Patterns

### Button States
```css
/* Disabled states */
.button:disabled {
    background: #ccc;
    color: #999;
    cursor: not-allowed;
    transform: none;
    box-shadow: none;
}

.button:disabled:hover {
    background: #ccc;
    transform: none;
}

/* Loading states */
.button.loading {
    position: relative;
    color: transparent;
}

.button.loading::after {
    content: '';
    position: absolute;
    width: 16px;
    height: 16px;
    top: 50%;
    left: 50%;
    margin-left: -8px;
    margin-top: -8px;
    border: 2px solid transparent;
    border-top-color: currentColor;
    border-radius: 50%;
    animation: spin 1s linear infinite;
}

@keyframes spin {
    to { transform: rotate(360deg); }
}
```

### Form Validation
```css
.form-input.error {
    border-color: #dc3545;
    box-shadow: 0 0 0 3px rgba(220,53,69,0.1);
}

.form-input.success {
    border-color: #28a745;
    box-shadow: 0 0 0 3px rgba(40,167,69,0.1);
}

.error-message {
    color: #dc3545;
    font-size: 12px;
    margin-top: 4px;
    display: flex;
    align-items: center;
    gap: 4px;
}

.success-message {
    color: #28a745;
    font-size: 12px;
    margin-top: 4px;
    display: flex;
    align-items: center;
    gap: 4px;
}
```

## Mobile-First Guidelines

### Touch Targets
- **Minimum Size**: 44px × 44px
- **Recommended**: 48px × 48px for primary actions
- **Spacing**: Minimum 8px between touch targets

### Scrolling & Content
- **Scroll Behavior**: Hide scrollbars with `-webkit-scrollbar: none`
- **Content Padding**: Ensure content doesn't overlap with navigation
- **Safe Areas**: Consider iPhone notch and bottom safe areas

### Performance
- **Images**: Use appropriate formats (PNG for logos, JPG for photos)
- **Transitions**: Limit to 0.2s for smooth interactions
- **Shadows**: Use sparingly, max 30px blur radius

## Technical Implementation

### Base HTML Template
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ETEN - [Screen Name]</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        'toyo-blue': '#0062B0',
                        'toyo-gray': '#7F7F7F',
                        'toyo-light-gray': '#727272'
                    }
                }
            }
        }
    </script>
    <style>
        body {
            background: #f0f0f0;
            font-family: 'Helvetica Neue', sans-serif;
        }
        
        .device-frame {
            width: 393px;
            height: 852px;
            background: #000;
            border-radius: 25px;
            padding: 2px;
            margin: 0 auto;
            box-shadow: 0 8px 30px rgba(0,0,0,0.3);
        }
        
        .screen-content {
            width: 100%;
            height: 100%;
            background: white;
            border-radius: 23px;
            overflow: hidden;
            position: relative;
        }
        
        .status-bar {
            height: 44px;
            background: white;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 15px;
            color: #333;
            font-size: 14px;
            font-weight: 600;
        }
        
        .main-content {
            height: calc(100% - 44px);
            overflow-y: auto;
            padding: 20px 15px;
        }
        
        .main-content::-webkit-scrollbar {
            display: none;
        }
        
        .main-content {
            -ms-overflow-style: none;
            scrollbar-width: none;
        }
    </style>
</head>
<body>
    <div class="device-frame">
        <div class="screen-content">
            <!-- Status Bar -->
            <div class="status-bar">
                <div>12:30</div>
                <div class="flex items-center gap-1">
                    <i class="fas fa-signal"></i>
                    <i class="fas fa-wifi"></i>
                    <i class="fas fa-battery-three-quarters"></i>
                </div>
            </div>
            
            <!-- Main Content -->
            <div class="main-content">
                <!-- Screen content goes here -->
            </div>
            
            <!-- Navigation (if applicable) -->
        </div>
    </div>
</body>
</html>
```

### CSS Framework Integration
- **TailwindCSS**: Via CDN for utility classes
- **FontAwesome**: For iconography
- **Custom CSS**: For component-specific styling

### Interactive Elements
- **Form Validation**: Client-side validation feedback
- **Button States**: Hover, active, disabled states
- **Loading States**: For form submissions
- **Error Handling**: User-friendly error messages

## Quality Standards

### Accessibility
- **WCAG 2.1 AA Compliance**
- **Semantic HTML**: Proper heading hierarchy
- **Alt Text**: For all images
- **Focus Management**: Visible focus indicators
- **Color Contrast**: Minimum 4.5:1 ratio

### Performance
- **Fast Loading**: Optimized assets
- **Smooth Interactions**: Hardware acceleration for animations
- **Responsive**: Adapts to different screen sizes
- **Progressive Enhancement**: Core functionality without JavaScript

### Consistency
- **Design System Adherence**: Follow all specifications
- **Code Standards**: Clean, maintainable HTML/CSS
- **Documentation**: Inline comments for complex components
- **Testing**: Cross-browser compatibility

## Content Spacing Examples

### Real-World Spacing Calculations

```css
/* Photo upload screen with fixed submit button */
.main-content {
    padding-bottom: 80px; /* 70px button + 10px margin */
}

/* Checklist screen with header + dual action buttons */
.main-content {
    height: calc(100% - 44px - 73px - 80px);
    padding: 20px 15px;
}

/* Claim list with header + search + FAB */
.main-content {
    height: calc(100% - 44px - 73px - 65px - 100px);
    padding: 16px 15px;
}

/* Dashboard with bottom navigation */
.main-content {
    height: calc(100% - 44px);
    padding: 20px 15px 110px 15px;
}
```

## Usage Guidelines

### When to Use Bottom Navigation
- Dashboard screens
- Main entry points
- Index/showcase files
- Screens without top headers

### When to Use Top Header Navigation
- Sub-screens with back navigation
- Detail views
- Form screens
- Modal-style interactions

### Content Spacing Decision Tree
1. **Has bottom navigation?** → Add 110px bottom padding
2. **Has sticky buttons?** → Add 80px bottom padding OR use height calc
3. **Has FAB?** → Add 100px bottom padding or ensure clear space
4. **Complex layout?** → Use height calc() accounting for all fixed elements
5. **Always** → Test scroll behavior and ensure last content item is visible

### Component Selection
- **Primary Buttons**: Main actions, form submissions
- **Secondary Buttons**: Alternative actions, cancellations
- **FAB**: Quick create actions, primary floating actions
- **Cards**: Content grouping, list items, complex data display
- **Badges**: Status indicators, counters, notifications
- **Search**: Filter/find functionality in lists
- **Progress**: Multi-step processes, completion tracking
- **Checklists**: Validation workflows, requirement tracking
- **Photo Upload**: Document capture, evidence collection
- **Icons**: Visual hierarchy, action indicators

### Interactive Guidelines
- **Form Validation**: Always provide immediate feedback
- **Button States**: Show loading, disabled, and success states
- **Card Actions**: Use event.stopPropagation() for nested clickable elements
- **Search**: Implement live filtering for better UX
- **Empty States**: Always provide helpful guidance when no data

### Accessibility Checklist
- Touch targets minimum 44px × 44px
- Color contrast minimum 4.5:1
- Focus indicators visible and clear
- Loading states announced to screen readers
- Error messages descriptive and helpful
- Alt text for all meaningful images

This design system ensures consistent, accessible, and maintainable UI across the entire TOYO TIRES ETEN application.