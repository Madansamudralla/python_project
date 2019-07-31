from selenium.webdriver.common.by import By

class RenewalPage:

    # SYSTEM OVERVIEW TAB
    SYSTEM_OVERVIEW = By.LINK_TEXT, 'System overview'

    # GLOBAL RENEWAL SETTINGS TAB
    GLOBAL_RENEWAL_SETTINGS = By.LINK_TEXT, 'Global renewal settings'

    #TAB ELEMENTS
    GRACE_PERIOD = By.ID, 'RenewalGracePeriod'
    EXPIRED_SUBSCRIPTIONS = By.ID, 'refresh_subscription_expired'
    PAST_DUE_SUBSCRIPTIONS = By.ID, 'refresh_subscription_past_due'
    ACTIVE_SUBSCRIPTIONS = By.ID, 'refresh_subscription_active'
    OVERWRITE_IMPACT = By.ID, 'rewrite_products_gp'

    USAGE_BILLING_INTERVAL = By.ID, 'input_1'
    RADIO_PREVIOUS_DAY = By.ID, 'RenewalLicenceStart_LICENSE'
    RADIO_RENEWAL_DAY = By.ID, 'RenewalLicenceStart_PAYMENT'
    RADIO_SEND_MAIL_TO_ALL = By.ID, 'DisableRenewalNotifications_ALL'
    RADIO_SEND_MAIL_TO_6MONTHS = By.ID, 'DisableRenewalNotifications_6MONTHS'

    ADD_NOTIFICATION = By.ID, 'manageNotificationSettingsShow'
    CANCEL_LICENCE_MAIL = By.ID, 'EnableCancelLicenceEmails'
    SAVE_BUTTON = By.ID, 'renewalSettingsSubmit'


    # RENEWAL DISCOUNTS TAB
    RENEWAL_DISCOUNTS = By.LINK_TEXT, 'Renewal discounts'

    #TAB ELEMENTS
    ADD_RENEWAL_DISCOUNT = By.LINK_TEXT, 'Add renewal discount'

    SEARCH_PROMOTION_TITLE = By.NAME, 'promotion_title'
    STATUS_ACTIVE = By.ID, 'promotions_active'
    STATUS_INACTIVE = By.ID, 'promotions_inactive'
    SEARCH_BUTTON = By.CLASS_NAME, 'btn btn-primary mt-1'

    #Add new renewal discount page
    ADD_PROMO_TITLE = By.ID, 'promotiontitle'
    ADD_PROMO_DESCRIPTION = By.ID, 'promotiondescription'
    ADD_PROMO_DISCOUNT_CODE = By.ID, 'coupon'
    ADD_PROMO_DISCOUNT_VALUE = By.ID, 'discount'
    ADD_PROMO_DISCOUNT_TYPE = By.ID, 'discounttype'
    ENABLE_DISCOUNT = By.ID, 'enabled_1'

    #Apply to
    FIRST_RENEWAL = By.ID, 'no_apply_renewal'
    ALL_RENEWAL = By.ID, 'apply_all_renewal'
    LIMITED_RENEWAL = By.ID, 'apply_number_renewal'
    LIMITED_RENEWAL_VALUE = By.ID, 'RecurringChargesNumber'
    SAVE_DISCOUNT = By.CLASS_NAME, 'btn btn-success  '
    BACK_BUTTON = By.CLASS_NAME, 'btn btn-default  '

    # IMPORT SUBSCRIPTIONS TAB
    IMPORT_SUBSCRIPTIONS = By.LINK_TEXT, 'Import subscriptions'

    # USAGE TAB
    USAGE = By.LINK_TEXT, 'Usage'

