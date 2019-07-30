from selenium.webdriver.common.by import By

class CrossSellingPageLocators:

    ADD_CAMPAIGN_BTN = By.CLASS_NAME, 'btn btn-primary'

    CAMPAIGNS_TAB = By.ID, '__tab_Campaigns'
    CROSS_SELLING_TAB = By.ID, '__tab_Cross-selling'

    # Search cross-selling campaigns section
    CAMPAIGN_TITLE = By.ID, 'campaign-title'
    # PRIMARY_PRODUCTS = tbd
    # ADDITIONAL_PRODUCTS = tbd
    CAMPAIGN_ACTIVE = By.ID, 'campaign-active'
    CAMPAIGN_DISABLED = By.ID, 'campaign-disabled'
    SEARCH_BUTTON = By.CLASS_NAME, 'btn btn-primary mt-1'

class AddCrossSellingCampaign:

    CAMPAIGNS_TAB = By.ID, '__tab_Campaigns'
    CROSS_SELLING_TAB = By.ID, '__tab_Cross-selling'

    # Campaigns tab

    CAMPAIGN_TITLE = By.ID, 'CampaignName'
    START_DATE = By.ID, 'dateRangeStart'
    END_DATE = By.ID, 'dateRangeEnd'
    DISPLAY_CROSS_CAMPAIGNS_IN = By.ID, 'display_type'
    DISPLAY_IN_RECEIPT = By.ID, 'display_type3'

    SEARCH_PRODUCTS = By.ID, 'master_filter'

    SAVE_BTN = By.CLASS_NAME, 'btn btn-success '

    # Cross-selling tab
    MAX_RECOMMENDED_PRODUCTS = By.NAME, 'max_display'
    MAX_THUMBNAIL_SIZE = By.NAME, 'max_size'
