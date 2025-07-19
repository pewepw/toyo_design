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
    padding: 0 2px;
    z-index: 100;
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

/* Main content padding to prevent overlap */
.main-content {
    padding-bottom: 100px; /* Space for fixed buttons */
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

### Component Selection
- **Primary Buttons**: Main actions, form submissions
- **Secondary Buttons**: Alternative actions, cancellations
- **Cards**: Content grouping, list items
- **Badges**: Status indicators, notifications
- **Icons**: Visual hierarchy, action indicators

This design system ensures consistent, accessible, and maintainable UI across the entire TOYO TIRES ETEN application.