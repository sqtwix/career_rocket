<style>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    .offers-container {
        max-width: 1280px;
        margin: 0 auto;
        padding: 40px 24px;
        font-family: 'Inter', sans-serif;
        background-color: #0A1929;
        color: #FFFFFF;
    }

    .offers-header {
        text-align: center;
        margin-bottom: 48px;
    }

    .offers-header h1 {
        font-size: 2.5rem;
        font-weight: 700;
        color: #E2852E;
        margin-bottom: 16px;
    }

    .offers-header p {
        font-size: 1.125rem;
        color: #ABE0F0;
        max-width: 600px;
        margin: 0 auto;
    }

    .packages-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 32px;
        margin: 32px 0;
    }

    .package-card {
        background: rgba(255, 255, 255, 0.05);
        border: 2px solid rgba(171, 224, 240, 0.1);
        border-radius: 24px;
        padding: 32px 24px;
        display: flex;
        flex-direction: column;
        position: relative;
    }

    .package-card.popular {
        border-color: #E2852E;
        background: rgba(226, 133, 46, 0.05);
    }

    .popular-badge {
        position: absolute;
        top: -12px;
        right: 20px;
        background: #E2852E;
        color: white;
        padding: 6px 20px;
        font-size: 14px;
        font-weight: 600;
        border-radius: 20px;
        border: 2px solid #F5C857;
    }

    .package-header {
        margin-bottom: 24px;
        padding-bottom: 24px;
        border-bottom: 2px solid rgba(171, 224, 240, 0.2);
    }

    .badge {
        display: inline-block;
        background: rgba(171, 224, 240, 0.1);
        border: 1px solid #ABE0F0;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.875rem;
        color: #ABE0F0;
        margin-bottom: 12px;
    }

    .package-name {
        font-size: 1.875rem;
        font-weight: 700;
        color: #E2852E;
        margin-bottom: 12px;
    }

    .package-price {
        display: flex;
        align-items: baseline;
        gap: 8px;
        margin-top: 16px;
    }

    .price-amount {
        font-size: 2.5rem;
        font-weight: 800;
        color: #FFFFFF;
    }

    .price-period {
        font-size: 1rem;
        color: #ABE0F0;
    }

    .package-description {
        color: #ABE0F0;
        margin: 16px 0 24px;
        line-height: 1.6;
    }

    .features-list {
        list-style: none;
        margin: 0 0 32px;
        flex-grow: 1;
    }

    .feature-item {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 16px;
        color: #FFFFFF;
    }

    .feature-icon {
        width: 20px;
        height: 20px;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
    }

    .feature-icon.check {
        color: #F5C857;
        font-weight: bold;
    }

    .feature-icon.circle {
        color: #ABE0F0;
    }

    .consultation-tag {
        background: rgba(245, 200, 87, 0.1);
        border: 1px solid #F5C857;
        color: #F5C857;
        font-size: 0.875rem;
        padding: 6px 12px;
        border-radius: 20px;
        display: inline-block;
        margin: 16px 0;
    }

    .btn {
        display: block;
        width: 100%;
        padding: 16px 24px;
        border-radius: 30px;
        font-weight: 600;
        font-size: 1.125rem;
        text-align: center;
        cursor: pointer;
        border: 2px solid #E2852E;
        background: transparent;
        color: #E2852E;
        transition: background-color 0.3s, color 0.3s;
    }

    .btn:hover {
        background: #E2852E;
        color: #0A1929;
    }

    .btn-primary {
        background: #E2852E;
        color: #0A1929;
        border: none;
    }

    .btn-primary:hover {
        background: #F5C857;
    }

    @media (max-width: 768px) {
        .offers-container {
            padding: 20px 16px;
        }
        
        .offers-header h1 {
            font-size: 2rem;
        }
        
        .packages-grid {
            gap: 24px;
        }
        
        .popular-badge {
            font-size: 12px;
            padding: 4px 16px;
        }
    }
</style>
