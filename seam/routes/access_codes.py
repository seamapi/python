from typing import Optional, Any, List, Dict, Union
import abc
from ..client import SeamHttpClient
from ..route import route_metadata
from ..null import Null
from ..resources import AccessCode
from .access_codes_simulate import AbstractAccessCodesSimulate, AccessCodesSimulate
from .access_codes_unmanaged import AbstractAccessCodesUnmanaged, AccessCodesUnmanaged


class AbstractAccessCodes(abc.ABC):

    @property
    @abc.abstractmethod
    def simulate(self) -> AbstractAccessCodesSimulate:
        raise NotImplementedError()

    @property
    @abc.abstractmethod
    def unmanaged(self) -> AbstractAccessCodesUnmanaged:
        raise NotImplementedError()

    @abc.abstractmethod
    def create(
        self,
        *,
        device_id: str,
        allow_external_modification: Optional[bool] = None,
        attempt_for_offline_device: Optional[bool] = None,
        code: Optional[str] = None,
        common_code_key: Optional[str] = None,
        ends_at: Optional[str] = None,
        is_external_modification_allowed: Optional[bool] = None,
        is_offline_access_code: Optional[bool] = None,
        is_one_time_use: Optional[bool] = None,
        max_time_rounding: Optional[str] = None,
        name: Optional[str] = None,
        prefer_native_scheduling: Optional[bool] = None,
        preferred_code_length: Optional[float] = None,
        starts_at: Optional[str] = None,
        use_backup_access_code_pool: Optional[bool] = None,
        use_offline_access_code: Optional[bool] = None,
    ) -> AccessCode:
        """Creates a new `access code <https://docs.seam.co/low-level-apis/access-codes>`_. For granting access, we recommend `Access Grants <https://docs.seam.co/use-cases/granting-access>`_ instead: they work across both standalone smart locks and access control systems and manage the underlying codes for you. Use this low-level endpoint only when you need direct control over a code on a single device, such as setting a custom PIN value.

        :param device_id: ID of the device for which you want to create the new access code.

        :param allow_external_modification: Indicates whether `external modification <https://docs.seam.co/low-level-apis/smart-locks/access-codes#external-modification>`_ of the code is allowed. Default: ``false``.

        :param attempt_for_offline_device:

        :param code: Code to be used for access.

        :param common_code_key: Key to identify access codes that should have the same code. Any two access codes with the same ``common_code_key`` are guaranteed to have the same ``code``. See also `Creating and Updating Multiple Linked Access Codes <https://docs.seam.co/low-level-apis/smart-locks/access-codes/creating-and-updating-multiple-linked-access-codes>`_.

        :param ends_at: Date and time at which the validity of the new access code ends, in `ISO 8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`_ format. Must be a time in the future and after ``starts_at``.

        :param is_external_modification_allowed: Indicates whether `external modification <https://docs.seam.co/low-level-apis/smart-locks/access-codes#external-modification>`_ of the code is allowed. Default: ``false``.

        :param is_offline_access_code: Indicates whether the access code is an `offline access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes/offline-access-codes>`_.

        :param is_one_time_use: Indicates whether the `offline access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes/offline-access-codes>`_ is a single-use access code.

        :param max_time_rounding: Maximum rounding adjustment. To create a daily-bound `offline access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes/offline-access-codes>`_ for devices that support this feature, set this parameter to ``1d``.

        :param name: Name of the new access code. Enables administrators and users to identify the access code easily, especially when there are numerous access codes.

        Note that the name provided on Seam is used to identify the code on Seam and is not necessarily the name that will appear in the lock provider's app or on the device. This is because lock providers may have constraints on names, such as length, uniqueness, or characters that can be used. In addition, some lock providers may break down names into components such as ``first_name`` and ``last_name``.

        To provide a consistent experience, Seam identifies the code on Seam by its name but may modify the name that appears on the lock provider's app or on the device. For example, Seam may add additional characters or truncate the name to meet provider constraints.

        To help your users identify codes set by Seam, Seam provides the name exactly as it appears on the lock provider's app or on the device as a separate property called ``appearance``. This is an object with a ``name`` property and, optionally, ``first_name`` and ``last_name`` properties (for providers that break down a name into components).

        :param prefer_native_scheduling: Indicates whether `native scheduling <https://docs.seam.co/low-level-apis/smart-locks/access-codes#native-scheduling>`_ should be used for time-bound codes when supported by the provider. Default: ``true``.

        :param preferred_code_length: Preferred code length. Only applicable if you do not specify a ``code``. If the affected device does not support the preferred code length, Seam reverts to using the shortest supported code length.

        :param starts_at: Date and time at which the validity of the new access code starts, in `ISO 8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`_ format.

        :param use_backup_access_code_pool: Indicates whether to use a `backup access code pool <https://docs.seam.co/low-level-apis/smart-locks/access-codes/backup-access-codes>`_ provided by Seam. If ``true``, you can use ```/access_codes/pull_backup_access_code`` <https://docs.seam.co/api/access_codes/pull_backup_access_code>`_.

        :param use_offline_access_code: Deprecated: Use ``is_offline_access_code`` instead.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def create_multiple(
        self,
        *,
        device_ids: List[str],
        allow_external_modification: Optional[bool] = None,
        attempt_for_offline_device: Optional[bool] = None,
        behavior_when_code_cannot_be_shared: Optional[str] = None,
        code: Optional[str] = None,
        ends_at: Optional[str] = None,
        is_external_modification_allowed: Optional[bool] = None,
        name: Optional[str] = None,
        prefer_native_scheduling: Optional[bool] = None,
        preferred_code_length: Optional[float] = None,
        starts_at: Optional[str] = None,
        use_backup_access_code_pool: Optional[bool] = None,
    ) -> List[AccessCode]:
        """Creates new `access codes <https://docs.seam.co/low-level-apis/smart-locks/access-codes>`_ that share a common code across multiple devices.

        Users with more than one door lock in a property may want to create groups of linked access codes, all of which have the same code (PIN). For example, a short-term rental host may want to provide guests the same PIN for both a front door lock and a back door lock.

        If you specify a custom code, Seam assigns this custom code to each of the resulting access codes. However, in this case, Seam does not link these access codes together with a ``common_code_key``. That is, ``common_code_key`` remains null for these access codes.

        If you want to change these access codes that are not linked by a ``common_code_key``, you cannot use ``/access_codes/update_multiple``. However, you can update each of these access codes individually, using ``/access_codes/update``.

        See also `Creating and Updating Multiple Linked Access Codes <https://docs.seam.co/low-level-apis/smart-locks/access-codes/creating-and-updating-multiple-linked-access-codes>`_.

        For granting a person access to a space, `Access Grants <https://docs.seam.co/use-cases/granting-access>`_ are the default and recommended approach and work across both standalone smart locks and access systems. Use the lower-level Access Codes API directly only when you specifically need to manage individual PIN codes.

        :param device_ids: IDs of the devices for which you want to create the new access codes.

        :param allow_external_modification: Indicates whether `external modification <https://docs.seam.co/low-level-apis/smart-locks/access-codes#external-modification>`_ of the code is allowed. Default: ``false``.

        :param attempt_for_offline_device:

        :param behavior_when_code_cannot_be_shared: Desired behavior if any device cannot share a code. If ``throw`` (default), no access codes will be created if any device cannot share a code. If ``create_random_code``, a random code will be created on devices that cannot share a code.

        :param code: Code to be used for access.

        :param ends_at: Date and time at which the validity of the new access code ends, in `ISO 8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`_ format. Must be a time in the future and after ``starts_at``.

        :param is_external_modification_allowed: Indicates whether `external modification <https://docs.seam.co/low-level-apis/smart-locks/access-codes#external-modification>`_ of the code is allowed. Default: ``false``.

        :param name: Name of the new access code. Enables administrators and users to identify the access code easily, especially when there are numerous access codes.

        Note that the name provided on Seam is used to identify the code on Seam and is not necessarily the name that will appear in the lock provider's app or on the device. This is because lock providers may have constraints on names, such as length, uniqueness, or characters that can be used. In addition, some lock providers may break down names into components such as ``first_name`` and ``last_name``.

        To provide a consistent experience, Seam identifies the code on Seam by its name but may modify the name that appears on the lock provider's app or on the device. For example, Seam may add additional characters or truncate the name to meet provider constraints.

        To help your users identify codes set by Seam, Seam provides the name exactly as it appears on the lock provider's app or on the device as a separate property called ``appearance``. This is an object with a ``name`` property and, optionally, ``first_name`` and ``last_name`` properties (for providers that break down a name into components).

        :param prefer_native_scheduling: Indicates whether `native scheduling <https://docs.seam.co/low-level-apis/smart-locks/access-codes#native-scheduling>`_ should be used for time-bound codes when supported by the provider. Default: ``true``.

        :param preferred_code_length: Preferred code length. If the affected devices do not support the preferred code length, Seam reverts to using the shortest supported code length.

        :param starts_at: Date and time at which the validity of the new access code starts, in `ISO 8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`_ format.

        :param use_backup_access_code_pool: Indicates whether to use a `backup access code pool <https://docs.seam.co/low-level-apis/smart-locks/access-codes/backup-access-codes>`_ provided by Seam. If ``true``, you can use ```/access_codes/pull_backup_access_code`` <https://docs.seam.co/api/access_codes/pull_backup_access_code>`_.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(self, *, access_code_id: str, device_id: Optional[str] = None) -> None:
        """Deletes an `access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes>`_.

        :param access_code_id: ID of the access code that you want to delete.

        :param device_id: ID of the device for which you want to delete the access code.

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def generate_code(self, *, device_id: str) -> AccessCode:
        """Generates a code for an `access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes>`_, given a device ID.

        :param device_id: ID of the device for which you want to generate a code.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def get(
        self,
        *,
        access_code_id: Optional[str] = None,
        code: Optional[str] = None,
        device_id: Optional[str] = None,
    ) -> AccessCode:
        """Returns a specified `access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes>`_.

        You must specify either ``access_code_id`` or both ``device_id`` and ``code``.

        :param access_code_id: ID of the access code that you want to get. You must specify either ``access_code_id`` or both ``device_id`` and ``code``.

        :param code: Code of the access code that you want to get. You must specify either ``access_code_id`` or both ``device_id`` and ``code``.

        :param device_id: ID of the device containing the access code that you want to get. You must specify either ``access_code_id`` or both ``device_id`` and ``code``.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
        *,
        access_code_ids: Optional[List[str]] = None,
        access_grant_id: Optional[str] = None,
        access_grant_key: Optional[str] = None,
        access_method_id: Optional[str] = None,
        customer_key: Optional[str] = None,
        device_id: Optional[str] = None,
        limit: Optional[float] = None,
        page_cursor: Optional[Union[str, Null]] = None,
        search: Optional[str] = None,
        user_identifier_key: Optional[str] = None,
    ) -> List[AccessCode]:
        """Returns a list of all `access codes <https://docs.seam.co/low-level-apis/smart-locks/access-codes>`_.

        Specify ``device_id``, ``access_code_ids``, ``access_method_id``, ``access_grant_id``, or ``access_grant_key``.

        :param access_code_ids: IDs of the access codes that you want to retrieve. Specify ``device_id``, ``access_code_ids``, ``access_method_id``, ``access_grant_id``, or ``access_grant_key``.

        :param access_grant_id: ID of the access grant for which you want to list access codes. Specify ``device_id``, ``access_code_ids``, ``access_method_id``, ``access_grant_id``, or ``access_grant_key``.

        :param access_grant_key: Key of the access grant for which you want to list access codes. Specify ``device_id``, ``access_code_ids``, ``access_method_id``, ``access_grant_id``, or ``access_grant_key``.

        :param access_method_id: ID of the access method for which you want to list access codes. Specify ``device_id``, ``access_code_ids``, ``access_method_id``, ``access_grant_id``, or ``access_grant_key``.

        :param customer_key: Customer key for which you want to list access codes.

        :param device_id: ID of the device for which you want to list access codes. Specify ``device_id``, ``access_code_ids``, ``access_method_id``, ``access_grant_id``, or ``access_grant_key``.

        :param limit: Numerical limit on the number of access codes to return.

        :param page_cursor: Identifies the specific page of results to return, obtained from the previous page's ``next_page_cursor``.

        :param search: String for which to search. Filters returned access codes to include all records that satisfy a partial match using ``name``, ``code`` or ``access_code_id``.

        :param user_identifier_key: Your user ID for the user by which to filter access codes.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def pull_backup_access_code(self, *, access_code_id: str) -> AccessCode:
        """Retrieves a backup access code for an `access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes>`_. See also `Managing Backup Access Codes <https://docs.seam.co/low-level-apis/smart-locks/access-codes/backup-access-codes>`_.

        A backup access code pool is a collection of pre-programmed access codes stored on a device, ready for use. These codes are programmed in addition to the regular access codes on Seam, serving as a safety net for any issues with the primary codes. If there's ever a complication with a primary access code—be it due to intermittent connectivity, manual removal from a device, or provider outages—a backup code can be retrieved. Its end time can then be adjusted to align with the original code, facilitating seamless and uninterrupted access.

        You can pull a backup access code from the pool at any time. These backup codes are guaranteed to work immediately and automatically programmed to be removed from the device after the access code ends.

        You can only pull backup access codes for time-bound access codes.

        Before pulling a backup access code, make sure that the device's ``properties.supports_backup_access_code_pool`` is ``true``. Then, to activate the backup pool, set ``use_backup_access_code_pool`` to ``true`` when creating an access code.

        :param access_code_id: ID of the access code for which you want to pull a backup access code.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def report_device_constraints(
        self,
        *,
        device_id: str,
        max_code_length: Optional[int] = None,
        min_code_length: Optional[int] = None,
        supported_code_lengths: Optional[List[float]] = None,
    ) -> None:
        """Enables you to report access code-related constraints for a device. Currently, supports reporting supported code length constraints for SmartThings devices.

        Specify either ``supported_code_lengths`` or ``min_code_length``/``max_code_length``.

        :param device_id: ID of the device for which you want to report constraints.

        :param max_code_length: Maximum supported code length as an integer between 4 and 20, inclusive. You can specify either ``min_code_length``/``max_code_length`` or ``supported_code_lengths``.

        :param min_code_length: Minimum supported code length as an integer between 4 and 20, inclusive. You can specify either ``min_code_length``/``max_code_length`` or ``supported_code_lengths``.

        :param supported_code_lengths: Array of supported code lengths as integers between 4 and 20, inclusive. You can specify either ``supported_code_lengths`` or ``min_code_length``/``max_code_length``.

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def update(
        self,
        *,
        access_code_id: str,
        allow_external_modification: Optional[bool] = None,
        attempt_for_offline_device: Optional[bool] = None,
        code: Optional[str] = None,
        device_id: Optional[str] = None,
        ends_at: Optional[str] = None,
        is_external_modification_allowed: Optional[bool] = None,
        is_managed: Optional[bool] = None,
        name: Optional[str] = None,
        starts_at: Optional[str] = None,
        type: Optional[str] = None,
    ) -> None:
        """Updates a specified active or upcoming `access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes>`_.

        See also `Modifying Access Codes <https://docs.seam.co/low-level-apis/smart-locks/access-codes/modifying-access-codes>`_.

        :param access_code_id: ID of the access code that you want to update.

        :param allow_external_modification: Indicates whether `external modification <https://docs.seam.co/low-level-apis/smart-locks/access-codes#external-modification>`_ of the code is allowed. Default: ``false``.

        :param attempt_for_offline_device:

        :param code: Code to be used for access.

        :param device_id: ID of the device containing the access code that you want to update.

        :param ends_at: Date and time at which the validity of the new access code ends, in `ISO 8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`_ format. Must be a time in the future and after ``starts_at``.

        :param is_external_modification_allowed: Indicates whether `external modification <https://docs.seam.co/low-level-apis/smart-locks/access-codes#external-modification>`_ of the code is allowed. Default: ``false``.

        :param is_managed: Indicates whether the access code is managed through Seam. Note that to convert an unmanaged access code into a managed access code, use ``/access_codes/unmanaged/convert_to_managed``.

        :param name: Name of the new access code. Enables administrators and users to identify the access code easily, especially when there are numerous access codes.

        Note that the name provided on Seam is used to identify the code on Seam and is not necessarily the name that will appear in the lock provider's app or on the device. This is because lock providers may have constraints on names, such as length, uniqueness, or characters that can be used. In addition, some lock providers may break down names into components such as ``first_name`` and ``last_name``.

        To provide a consistent experience, Seam identifies the code on Seam by its name but may modify the name that appears on the lock provider's app or on the device. For example, Seam may add additional characters or truncate the name to meet provider constraints.

        To help your users identify codes set by Seam, Seam provides the name exactly as it appears on the lock provider's app or on the device as a separate property called ``appearance``. This is an object with a ``name`` property and, optionally, ``first_name`` and ``last_name`` properties (for providers that break down a name into components).

        :param starts_at: Date and time at which the validity of the new access code starts, in `ISO 8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`_ format.

        :param type: Type to which you want to convert the access code. To convert a time-bound access code to an ongoing access code, set ``type`` to ``ongoing``. See also `Changing a time-bound access code to permanent access <https://docs.seam.co/low-level-apis/smart-locks/access-codes/modifying-access-codes#special-case-2-changing-a-time-bound-access-code-to-permanent-access>`_.

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def update_multiple(
        self,
        *,
        common_code_key: str,
        ends_at: Optional[str] = None,
        name: Optional[str] = None,
        starts_at: Optional[str] = None,
    ) -> None:
        """Updates `access codes <https://docs.seam.co/low-level-apis/smart-locks/access-codes>`_ that share a common code across multiple devices.

        Specify the ``common_code_key`` to identify the set of access codes that you want to update.

        See also `Update Linked Access Codes <https://docs.seam.co/low-level-apis/smart-locks/access-codes/creating-and-updating-multiple-linked-access-codes#update-linked-access-codes>`_.

        :param common_code_key: Key that links the group of access codes, assigned on creation by ``/access_codes/create_multiple``.

        :param ends_at: Date and time at which the validity of the new access code ends, in `ISO 8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`_ format. Must be a time in the future and after ``starts_at``.

        :param name: Name of the new access code. Enables administrators and users to identify the access code easily, especially when there are numerous access codes.

        Note that the name provided on Seam is used to identify the code on Seam and is not necessarily the name that will appear in the lock provider's app or on the device. This is because lock providers may have constraints on names, such as length, uniqueness, or characters that can be used. In addition, some lock providers may break down names into components such as ``first_name`` and ``last_name``.

        To provide a consistent experience, Seam identifies the code on Seam by its name but may modify the name that appears on the lock provider's app or on the device. For example, Seam may add additional characters or truncate the name to meet provider constraints.

        To help your users identify codes set by Seam, Seam provides the name exactly as it appears on the lock provider's app or on the device as a separate property called ``appearance``. This is an object with a ``name`` property and, optionally, ``first_name`` and ``last_name`` properties (for providers that break down a name into components).

        :param starts_at: Date and time at which the validity of the new access code starts, in `ISO 8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`_ format.

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()


class AccessCodes(AbstractAccessCodes):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults
        self._simulate = AccessCodesSimulate(client=client, defaults=defaults)
        self._unmanaged = AccessCodesUnmanaged(client=client, defaults=defaults)

    @property
    def simulate(self) -> AccessCodesSimulate:
        return self._simulate

    @property
    def unmanaged(self) -> AccessCodesUnmanaged:
        return self._unmanaged

    @route_metadata(
        path="/access_codes/create", has_required_parameters=True, has_pagination=False
    )
    def create(
        self,
        *,
        device_id: str,
        allow_external_modification: Optional[bool] = None,
        attempt_for_offline_device: Optional[bool] = None,
        code: Optional[str] = None,
        common_code_key: Optional[str] = None,
        ends_at: Optional[str] = None,
        is_external_modification_allowed: Optional[bool] = None,
        is_offline_access_code: Optional[bool] = None,
        is_one_time_use: Optional[bool] = None,
        max_time_rounding: Optional[str] = None,
        name: Optional[str] = None,
        prefer_native_scheduling: Optional[bool] = None,
        preferred_code_length: Optional[float] = None,
        starts_at: Optional[str] = None,
        use_backup_access_code_pool: Optional[bool] = None,
        use_offline_access_code: Optional[bool] = None,
    ) -> AccessCode:
        """Creates a new `access code <https://docs.seam.co/low-level-apis/access-codes>`_. For granting access, we recommend `Access Grants <https://docs.seam.co/use-cases/granting-access>`_ instead: they work across both standalone smart locks and access control systems and manage the underlying codes for you. Use this low-level endpoint only when you need direct control over a code on a single device, such as setting a custom PIN value.

        :param device_id: ID of the device for which you want to create the new access code.

        :param allow_external_modification: Indicates whether `external modification <https://docs.seam.co/low-level-apis/smart-locks/access-codes#external-modification>`_ of the code is allowed. Default: ``false``.

        :param attempt_for_offline_device:

        :param code: Code to be used for access.

        :param common_code_key: Key to identify access codes that should have the same code. Any two access codes with the same ``common_code_key`` are guaranteed to have the same ``code``. See also `Creating and Updating Multiple Linked Access Codes <https://docs.seam.co/low-level-apis/smart-locks/access-codes/creating-and-updating-multiple-linked-access-codes>`_.

        :param ends_at: Date and time at which the validity of the new access code ends, in `ISO 8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`_ format. Must be a time in the future and after ``starts_at``.

        :param is_external_modification_allowed: Indicates whether `external modification <https://docs.seam.co/low-level-apis/smart-locks/access-codes#external-modification>`_ of the code is allowed. Default: ``false``.

        :param is_offline_access_code: Indicates whether the access code is an `offline access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes/offline-access-codes>`_.

        :param is_one_time_use: Indicates whether the `offline access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes/offline-access-codes>`_ is a single-use access code.

        :param max_time_rounding: Maximum rounding adjustment. To create a daily-bound `offline access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes/offline-access-codes>`_ for devices that support this feature, set this parameter to ``1d``.

        :param name: Name of the new access code. Enables administrators and users to identify the access code easily, especially when there are numerous access codes.

        Note that the name provided on Seam is used to identify the code on Seam and is not necessarily the name that will appear in the lock provider's app or on the device. This is because lock providers may have constraints on names, such as length, uniqueness, or characters that can be used. In addition, some lock providers may break down names into components such as ``first_name`` and ``last_name``.

        To provide a consistent experience, Seam identifies the code on Seam by its name but may modify the name that appears on the lock provider's app or on the device. For example, Seam may add additional characters or truncate the name to meet provider constraints.

        To help your users identify codes set by Seam, Seam provides the name exactly as it appears on the lock provider's app or on the device as a separate property called ``appearance``. This is an object with a ``name`` property and, optionally, ``first_name`` and ``last_name`` properties (for providers that break down a name into components).

        :param prefer_native_scheduling: Indicates whether `native scheduling <https://docs.seam.co/low-level-apis/smart-locks/access-codes#native-scheduling>`_ should be used for time-bound codes when supported by the provider. Default: ``true``.

        :param preferred_code_length: Preferred code length. Only applicable if you do not specify a ``code``. If the affected device does not support the preferred code length, Seam reverts to using the shortest supported code length.

        :param starts_at: Date and time at which the validity of the new access code starts, in `ISO 8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`_ format.

        :param use_backup_access_code_pool: Indicates whether to use a `backup access code pool <https://docs.seam.co/low-level-apis/smart-locks/access-codes/backup-access-codes>`_ provided by Seam. If ``true``, you can use ```/access_codes/pull_backup_access_code`` <https://docs.seam.co/api/access_codes/pull_backup_access_code>`_.

        :param use_offline_access_code: Deprecated: Use ``is_offline_access_code`` instead.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        json_payload: Dict[str, Any] = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if allow_external_modification is not None:
            json_payload["allow_external_modification"] = allow_external_modification
        if attempt_for_offline_device is not None:
            json_payload["attempt_for_offline_device"] = attempt_for_offline_device
        if code is not None:
            json_payload["code"] = code
        if common_code_key is not None:
            json_payload["common_code_key"] = common_code_key
        if ends_at is not None:
            json_payload["ends_at"] = ends_at
        if is_external_modification_allowed is not None:
            json_payload["is_external_modification_allowed"] = (
                is_external_modification_allowed
            )
        if is_offline_access_code is not None:
            json_payload["is_offline_access_code"] = is_offline_access_code
        if is_one_time_use is not None:
            json_payload["is_one_time_use"] = is_one_time_use
        if max_time_rounding is not None:
            json_payload["max_time_rounding"] = max_time_rounding
        if name is not None:
            json_payload["name"] = name
        if prefer_native_scheduling is not None:
            json_payload["prefer_native_scheduling"] = prefer_native_scheduling
        if preferred_code_length is not None:
            json_payload["preferred_code_length"] = preferred_code_length
        if starts_at is not None:
            json_payload["starts_at"] = starts_at
        if use_backup_access_code_pool is not None:
            json_payload["use_backup_access_code_pool"] = use_backup_access_code_pool
        if use_offline_access_code is not None:
            json_payload["use_offline_access_code"] = use_offline_access_code

        if not json_payload:
            raise ValueError(
                "At least one parameter is required for /access_codes/create"
            )

        res = self.client.post("/access_codes/create", json=json_payload)

        return AccessCode.from_dict(res["access_code"])

    @route_metadata(
        path="/access_codes/create_multiple",
        has_required_parameters=True,
        has_pagination=False,
    )
    def create_multiple(
        self,
        *,
        device_ids: List[str],
        allow_external_modification: Optional[bool] = None,
        attempt_for_offline_device: Optional[bool] = None,
        behavior_when_code_cannot_be_shared: Optional[str] = None,
        code: Optional[str] = None,
        ends_at: Optional[str] = None,
        is_external_modification_allowed: Optional[bool] = None,
        name: Optional[str] = None,
        prefer_native_scheduling: Optional[bool] = None,
        preferred_code_length: Optional[float] = None,
        starts_at: Optional[str] = None,
        use_backup_access_code_pool: Optional[bool] = None,
    ) -> List[AccessCode]:
        """Creates new `access codes <https://docs.seam.co/low-level-apis/smart-locks/access-codes>`_ that share a common code across multiple devices.

        Users with more than one door lock in a property may want to create groups of linked access codes, all of which have the same code (PIN). For example, a short-term rental host may want to provide guests the same PIN for both a front door lock and a back door lock.

        If you specify a custom code, Seam assigns this custom code to each of the resulting access codes. However, in this case, Seam does not link these access codes together with a ``common_code_key``. That is, ``common_code_key`` remains null for these access codes.

        If you want to change these access codes that are not linked by a ``common_code_key``, you cannot use ``/access_codes/update_multiple``. However, you can update each of these access codes individually, using ``/access_codes/update``.

        See also `Creating and Updating Multiple Linked Access Codes <https://docs.seam.co/low-level-apis/smart-locks/access-codes/creating-and-updating-multiple-linked-access-codes>`_.

        For granting a person access to a space, `Access Grants <https://docs.seam.co/use-cases/granting-access>`_ are the default and recommended approach and work across both standalone smart locks and access systems. Use the lower-level Access Codes API directly only when you specifically need to manage individual PIN codes.

        :param device_ids: IDs of the devices for which you want to create the new access codes.

        :param allow_external_modification: Indicates whether `external modification <https://docs.seam.co/low-level-apis/smart-locks/access-codes#external-modification>`_ of the code is allowed. Default: ``false``.

        :param attempt_for_offline_device:

        :param behavior_when_code_cannot_be_shared: Desired behavior if any device cannot share a code. If ``throw`` (default), no access codes will be created if any device cannot share a code. If ``create_random_code``, a random code will be created on devices that cannot share a code.

        :param code: Code to be used for access.

        :param ends_at: Date and time at which the validity of the new access code ends, in `ISO 8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`_ format. Must be a time in the future and after ``starts_at``.

        :param is_external_modification_allowed: Indicates whether `external modification <https://docs.seam.co/low-level-apis/smart-locks/access-codes#external-modification>`_ of the code is allowed. Default: ``false``.

        :param name: Name of the new access code. Enables administrators and users to identify the access code easily, especially when there are numerous access codes.

        Note that the name provided on Seam is used to identify the code on Seam and is not necessarily the name that will appear in the lock provider's app or on the device. This is because lock providers may have constraints on names, such as length, uniqueness, or characters that can be used. In addition, some lock providers may break down names into components such as ``first_name`` and ``last_name``.

        To provide a consistent experience, Seam identifies the code on Seam by its name but may modify the name that appears on the lock provider's app or on the device. For example, Seam may add additional characters or truncate the name to meet provider constraints.

        To help your users identify codes set by Seam, Seam provides the name exactly as it appears on the lock provider's app or on the device as a separate property called ``appearance``. This is an object with a ``name`` property and, optionally, ``first_name`` and ``last_name`` properties (for providers that break down a name into components).

        :param prefer_native_scheduling: Indicates whether `native scheduling <https://docs.seam.co/low-level-apis/smart-locks/access-codes#native-scheduling>`_ should be used for time-bound codes when supported by the provider. Default: ``true``.

        :param preferred_code_length: Preferred code length. If the affected devices do not support the preferred code length, Seam reverts to using the shortest supported code length.

        :param starts_at: Date and time at which the validity of the new access code starts, in `ISO 8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`_ format.

        :param use_backup_access_code_pool: Indicates whether to use a `backup access code pool <https://docs.seam.co/low-level-apis/smart-locks/access-codes/backup-access-codes>`_ provided by Seam. If ``true``, you can use ```/access_codes/pull_backup_access_code`` <https://docs.seam.co/api/access_codes/pull_backup_access_code>`_.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        json_payload: Dict[str, Any] = {}

        if device_ids is not None:
            json_payload["device_ids"] = device_ids
        if allow_external_modification is not None:
            json_payload["allow_external_modification"] = allow_external_modification
        if attempt_for_offline_device is not None:
            json_payload["attempt_for_offline_device"] = attempt_for_offline_device
        if behavior_when_code_cannot_be_shared is not None:
            json_payload["behavior_when_code_cannot_be_shared"] = (
                behavior_when_code_cannot_be_shared
            )
        if code is not None:
            json_payload["code"] = code
        if ends_at is not None:
            json_payload["ends_at"] = ends_at
        if is_external_modification_allowed is not None:
            json_payload["is_external_modification_allowed"] = (
                is_external_modification_allowed
            )
        if name is not None:
            json_payload["name"] = name
        if prefer_native_scheduling is not None:
            json_payload["prefer_native_scheduling"] = prefer_native_scheduling
        if preferred_code_length is not None:
            json_payload["preferred_code_length"] = preferred_code_length
        if starts_at is not None:
            json_payload["starts_at"] = starts_at
        if use_backup_access_code_pool is not None:
            json_payload["use_backup_access_code_pool"] = use_backup_access_code_pool

        if not json_payload:
            raise ValueError(
                "At least one parameter is required for /access_codes/create_multiple"
            )

        res = self.client.put("/access_codes/create_multiple", json=json_payload)

        return [AccessCode.from_dict(item) for item in res["access_codes"]]

    @route_metadata(
        path="/access_codes/delete", has_required_parameters=True, has_pagination=False
    )
    def delete(self, *, access_code_id: str, device_id: Optional[str] = None) -> None:
        """Deletes an `access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes>`_.

        :param access_code_id: ID of the access code that you want to delete.

        :param device_id: ID of the device for which you want to delete the access code.

        :raises ValueError: At least one parameter must be provided."""
        params: Dict[str, Any] = {}

        if access_code_id is not None:
            params["access_code_id"] = access_code_id
        if device_id is not None:
            params["device_id"] = device_id

        if not params:
            raise ValueError(
                "At least one parameter is required for /access_codes/delete"
            )

        self.client.delete("/access_codes/delete", params=params)

        return None

    @route_metadata(
        path="/access_codes/generate_code",
        has_required_parameters=True,
        has_pagination=False,
    )
    def generate_code(self, *, device_id: str) -> AccessCode:
        """Generates a code for an `access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes>`_, given a device ID.

        :param device_id: ID of the device for which you want to generate a code.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        params: Dict[str, Any] = {}

        if device_id is not None:
            params["device_id"] = device_id

        if not params:
            raise ValueError(
                "At least one parameter is required for /access_codes/generate_code"
            )

        res = self.client.get("/access_codes/generate_code", params=params)

        return AccessCode.from_dict(res["generated_code"])

    @route_metadata(
        path="/access_codes/get", has_required_parameters=True, has_pagination=False
    )
    def get(
        self,
        *,
        access_code_id: Optional[str] = None,
        code: Optional[str] = None,
        device_id: Optional[str] = None,
    ) -> AccessCode:
        """Returns a specified `access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes>`_.

        You must specify either ``access_code_id`` or both ``device_id`` and ``code``.

        :param access_code_id: ID of the access code that you want to get. You must specify either ``access_code_id`` or both ``device_id`` and ``code``.

        :param code: Code of the access code that you want to get. You must specify either ``access_code_id`` or both ``device_id`` and ``code``.

        :param device_id: ID of the device containing the access code that you want to get. You must specify either ``access_code_id`` or both ``device_id`` and ``code``.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        params: Dict[str, Any] = {}

        if access_code_id is not None:
            params["access_code_id"] = access_code_id
        if code is not None:
            params["code"] = code
        if device_id is not None:
            params["device_id"] = device_id

        if not params:
            raise ValueError("At least one parameter is required for /access_codes/get")

        res = self.client.get("/access_codes/get", params=params)

        return AccessCode.from_dict(res["access_code"])

    @route_metadata(
        path="/access_codes/list", has_required_parameters=True, has_pagination=True
    )
    def list(
        self,
        *,
        access_code_ids: Optional[List[str]] = None,
        access_grant_id: Optional[str] = None,
        access_grant_key: Optional[str] = None,
        access_method_id: Optional[str] = None,
        customer_key: Optional[str] = None,
        device_id: Optional[str] = None,
        limit: Optional[float] = None,
        page_cursor: Optional[Union[str, Null]] = None,
        search: Optional[str] = None,
        user_identifier_key: Optional[str] = None,
    ) -> List[AccessCode]:
        """Returns a list of all `access codes <https://docs.seam.co/low-level-apis/smart-locks/access-codes>`_.

        Specify ``device_id``, ``access_code_ids``, ``access_method_id``, ``access_grant_id``, or ``access_grant_key``.

        :param access_code_ids: IDs of the access codes that you want to retrieve. Specify ``device_id``, ``access_code_ids``, ``access_method_id``, ``access_grant_id``, or ``access_grant_key``.

        :param access_grant_id: ID of the access grant for which you want to list access codes. Specify ``device_id``, ``access_code_ids``, ``access_method_id``, ``access_grant_id``, or ``access_grant_key``.

        :param access_grant_key: Key of the access grant for which you want to list access codes. Specify ``device_id``, ``access_code_ids``, ``access_method_id``, ``access_grant_id``, or ``access_grant_key``.

        :param access_method_id: ID of the access method for which you want to list access codes. Specify ``device_id``, ``access_code_ids``, ``access_method_id``, ``access_grant_id``, or ``access_grant_key``.

        :param customer_key: Customer key for which you want to list access codes.

        :param device_id: ID of the device for which you want to list access codes. Specify ``device_id``, ``access_code_ids``, ``access_method_id``, ``access_grant_id``, or ``access_grant_key``.

        :param limit: Numerical limit on the number of access codes to return.

        :param page_cursor: Identifies the specific page of results to return, obtained from the previous page's ``next_page_cursor``.

        :param search: String for which to search. Filters returned access codes to include all records that satisfy a partial match using ``name``, ``code`` or ``access_code_id``.

        :param user_identifier_key: Your user ID for the user by which to filter access codes.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        json_payload: Dict[str, Any] = {}

        if access_code_ids is not None:
            json_payload["access_code_ids"] = access_code_ids
        if access_grant_id is not None:
            json_payload["access_grant_id"] = access_grant_id
        if access_grant_key is not None:
            json_payload["access_grant_key"] = access_grant_key
        if access_method_id is not None:
            json_payload["access_method_id"] = access_method_id
        if customer_key is not None:
            json_payload["customer_key"] = customer_key
        if device_id is not None:
            json_payload["device_id"] = device_id
        if limit is not None:
            json_payload["limit"] = limit
        if page_cursor is not None:
            json_payload["page_cursor"] = page_cursor
        if search is not None:
            json_payload["search"] = search
        if user_identifier_key is not None:
            json_payload["user_identifier_key"] = user_identifier_key

        if not json_payload:
            raise ValueError(
                "At least one parameter is required for /access_codes/list"
            )

        res = self.client.post("/access_codes/list", json=json_payload)

        return [AccessCode.from_dict(item) for item in res["access_codes"]]

    @route_metadata(
        path="/access_codes/pull_backup_access_code",
        has_required_parameters=True,
        has_pagination=False,
    )
    def pull_backup_access_code(self, *, access_code_id: str) -> AccessCode:
        """Retrieves a backup access code for an `access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes>`_. See also `Managing Backup Access Codes <https://docs.seam.co/low-level-apis/smart-locks/access-codes/backup-access-codes>`_.

        A backup access code pool is a collection of pre-programmed access codes stored on a device, ready for use. These codes are programmed in addition to the regular access codes on Seam, serving as a safety net for any issues with the primary codes. If there's ever a complication with a primary access code—be it due to intermittent connectivity, manual removal from a device, or provider outages—a backup code can be retrieved. Its end time can then be adjusted to align with the original code, facilitating seamless and uninterrupted access.

        You can pull a backup access code from the pool at any time. These backup codes are guaranteed to work immediately and automatically programmed to be removed from the device after the access code ends.

        You can only pull backup access codes for time-bound access codes.

        Before pulling a backup access code, make sure that the device's ``properties.supports_backup_access_code_pool`` is ``true``. Then, to activate the backup pool, set ``use_backup_access_code_pool`` to ``true`` when creating an access code.

        :param access_code_id: ID of the access code for which you want to pull a backup access code.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        json_payload: Dict[str, Any] = {}

        if access_code_id is not None:
            json_payload["access_code_id"] = access_code_id

        if not json_payload:
            raise ValueError(
                "At least one parameter is required for /access_codes/pull_backup_access_code"
            )

        res = self.client.post(
            "/access_codes/pull_backup_access_code", json=json_payload
        )

        return AccessCode.from_dict(res["access_code"])

    @route_metadata(
        path="/access_codes/report_device_constraints",
        has_required_parameters=True,
        has_pagination=False,
    )
    def report_device_constraints(
        self,
        *,
        device_id: str,
        max_code_length: Optional[int] = None,
        min_code_length: Optional[int] = None,
        supported_code_lengths: Optional[List[float]] = None,
    ) -> None:
        """Enables you to report access code-related constraints for a device. Currently, supports reporting supported code length constraints for SmartThings devices.

        Specify either ``supported_code_lengths`` or ``min_code_length``/``max_code_length``.

        :param device_id: ID of the device for which you want to report constraints.

        :param max_code_length: Maximum supported code length as an integer between 4 and 20, inclusive. You can specify either ``min_code_length``/``max_code_length`` or ``supported_code_lengths``.

        :param min_code_length: Minimum supported code length as an integer between 4 and 20, inclusive. You can specify either ``min_code_length``/``max_code_length`` or ``supported_code_lengths``.

        :param supported_code_lengths: Array of supported code lengths as integers between 4 and 20, inclusive. You can specify either ``supported_code_lengths`` or ``min_code_length``/``max_code_length``.

        :raises ValueError: At least one parameter must be provided."""
        json_payload: Dict[str, Any] = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if max_code_length is not None:
            json_payload["max_code_length"] = max_code_length
        if min_code_length is not None:
            json_payload["min_code_length"] = min_code_length
        if supported_code_lengths is not None:
            json_payload["supported_code_lengths"] = supported_code_lengths

        if not json_payload:
            raise ValueError(
                "At least one parameter is required for /access_codes/report_device_constraints"
            )

        self.client.post("/access_codes/report_device_constraints", json=json_payload)

        return None

    @route_metadata(
        path="/access_codes/update", has_required_parameters=True, has_pagination=False
    )
    def update(
        self,
        *,
        access_code_id: str,
        allow_external_modification: Optional[bool] = None,
        attempt_for_offline_device: Optional[bool] = None,
        code: Optional[str] = None,
        device_id: Optional[str] = None,
        ends_at: Optional[str] = None,
        is_external_modification_allowed: Optional[bool] = None,
        is_managed: Optional[bool] = None,
        name: Optional[str] = None,
        starts_at: Optional[str] = None,
        type: Optional[str] = None,
    ) -> None:
        """Updates a specified active or upcoming `access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes>`_.

        See also `Modifying Access Codes <https://docs.seam.co/low-level-apis/smart-locks/access-codes/modifying-access-codes>`_.

        :param access_code_id: ID of the access code that you want to update.

        :param allow_external_modification: Indicates whether `external modification <https://docs.seam.co/low-level-apis/smart-locks/access-codes#external-modification>`_ of the code is allowed. Default: ``false``.

        :param attempt_for_offline_device:

        :param code: Code to be used for access.

        :param device_id: ID of the device containing the access code that you want to update.

        :param ends_at: Date and time at which the validity of the new access code ends, in `ISO 8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`_ format. Must be a time in the future and after ``starts_at``.

        :param is_external_modification_allowed: Indicates whether `external modification <https://docs.seam.co/low-level-apis/smart-locks/access-codes#external-modification>`_ of the code is allowed. Default: ``false``.

        :param is_managed: Indicates whether the access code is managed through Seam. Note that to convert an unmanaged access code into a managed access code, use ``/access_codes/unmanaged/convert_to_managed``.

        :param name: Name of the new access code. Enables administrators and users to identify the access code easily, especially when there are numerous access codes.

        Note that the name provided on Seam is used to identify the code on Seam and is not necessarily the name that will appear in the lock provider's app or on the device. This is because lock providers may have constraints on names, such as length, uniqueness, or characters that can be used. In addition, some lock providers may break down names into components such as ``first_name`` and ``last_name``.

        To provide a consistent experience, Seam identifies the code on Seam by its name but may modify the name that appears on the lock provider's app or on the device. For example, Seam may add additional characters or truncate the name to meet provider constraints.

        To help your users identify codes set by Seam, Seam provides the name exactly as it appears on the lock provider's app or on the device as a separate property called ``appearance``. This is an object with a ``name`` property and, optionally, ``first_name`` and ``last_name`` properties (for providers that break down a name into components).

        :param starts_at: Date and time at which the validity of the new access code starts, in `ISO 8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`_ format.

        :param type: Type to which you want to convert the access code. To convert a time-bound access code to an ongoing access code, set ``type`` to ``ongoing``. See also `Changing a time-bound access code to permanent access <https://docs.seam.co/low-level-apis/smart-locks/access-codes/modifying-access-codes#special-case-2-changing-a-time-bound-access-code-to-permanent-access>`_.

        :raises ValueError: At least one parameter must be provided."""
        json_payload: Dict[str, Any] = {}

        if access_code_id is not None:
            json_payload["access_code_id"] = access_code_id
        if allow_external_modification is not None:
            json_payload["allow_external_modification"] = allow_external_modification
        if attempt_for_offline_device is not None:
            json_payload["attempt_for_offline_device"] = attempt_for_offline_device
        if code is not None:
            json_payload["code"] = code
        if device_id is not None:
            json_payload["device_id"] = device_id
        if ends_at is not None:
            json_payload["ends_at"] = ends_at
        if is_external_modification_allowed is not None:
            json_payload["is_external_modification_allowed"] = (
                is_external_modification_allowed
            )
        if is_managed is not None:
            json_payload["is_managed"] = is_managed
        if name is not None:
            json_payload["name"] = name
        if starts_at is not None:
            json_payload["starts_at"] = starts_at
        if type is not None:
            json_payload["type"] = type

        if not json_payload:
            raise ValueError(
                "At least one parameter is required for /access_codes/update"
            )

        self.client.put("/access_codes/update", json=json_payload)

        return None

    @route_metadata(
        path="/access_codes/update_multiple",
        has_required_parameters=True,
        has_pagination=False,
    )
    def update_multiple(
        self,
        *,
        common_code_key: str,
        ends_at: Optional[str] = None,
        name: Optional[str] = None,
        starts_at: Optional[str] = None,
    ) -> None:
        """Updates `access codes <https://docs.seam.co/low-level-apis/smart-locks/access-codes>`_ that share a common code across multiple devices.

        Specify the ``common_code_key`` to identify the set of access codes that you want to update.

        See also `Update Linked Access Codes <https://docs.seam.co/low-level-apis/smart-locks/access-codes/creating-and-updating-multiple-linked-access-codes#update-linked-access-codes>`_.

        :param common_code_key: Key that links the group of access codes, assigned on creation by ``/access_codes/create_multiple``.

        :param ends_at: Date and time at which the validity of the new access code ends, in `ISO 8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`_ format. Must be a time in the future and after ``starts_at``.

        :param name: Name of the new access code. Enables administrators and users to identify the access code easily, especially when there are numerous access codes.

        Note that the name provided on Seam is used to identify the code on Seam and is not necessarily the name that will appear in the lock provider's app or on the device. This is because lock providers may have constraints on names, such as length, uniqueness, or characters that can be used. In addition, some lock providers may break down names into components such as ``first_name`` and ``last_name``.

        To provide a consistent experience, Seam identifies the code on Seam by its name but may modify the name that appears on the lock provider's app or on the device. For example, Seam may add additional characters or truncate the name to meet provider constraints.

        To help your users identify codes set by Seam, Seam provides the name exactly as it appears on the lock provider's app or on the device as a separate property called ``appearance``. This is an object with a ``name`` property and, optionally, ``first_name`` and ``last_name`` properties (for providers that break down a name into components).

        :param starts_at: Date and time at which the validity of the new access code starts, in `ISO 8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`_ format.

        :raises ValueError: At least one parameter must be provided."""
        json_payload: Dict[str, Any] = {}

        if common_code_key is not None:
            json_payload["common_code_key"] = common_code_key
        if ends_at is not None:
            json_payload["ends_at"] = ends_at
        if name is not None:
            json_payload["name"] = name
        if starts_at is not None:
            json_payload["starts_at"] = starts_at

        if not json_payload:
            raise ValueError(
                "At least one parameter is required for /access_codes/update_multiple"
            )

        self.client.patch("/access_codes/update_multiple", json=json_payload)

        return None
