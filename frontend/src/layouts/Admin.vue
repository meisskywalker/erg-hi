<script setup>
import LogoutIcon from '../components/icons/LogoutIcon.vue';
import ProductIcon from '../components/icons/ProductIcon.vue';
import AccountIcon from '../components/icons/AccountIcon.vue';
import MenuIcon from '../components/icons/MenuIcon.vue';
import AdminNavbar from '../components/admin/Navbar.vue';
import AdminSidenav from '../components/admin/Sidenav.vue';
</script>

<template>
  <div class="min-h-screen w-full flex bg-grey-300 p-2">
    <admin-sidenav>
      <template #menus>
        <div class="flex gap-4 cursor-pointer group">
          <product-icon
            size="24"
            class="transition duration-200 group-hover:text-brand-600"
          />
          <span
            class="text-md text-grey-900 font-medium transition duration-200 group-hover:text-brand-600"
            >Products</span
          >
        </div>
        <div class="flex gap-4">
          <account-icon size="24" />
          <span class="text-md text-grey-900 font-medium">Accounts</span>
        </div>
      </template>
      <template #bottom-menu>
        <logout-icon size="20" />
        <span class="text-md font-medium">Logout</span>
      </template>
    </admin-sidenav>
    <div class="w-full overflow-hidden">
      <admin-navbar>
        <template #left>
          <menu-icon size="26" clickable />
        </template>
        <template #right>
          <div class="flex items-center gap-2">
            <account-icon size="26" />
            <span>Bayu Prima</span>
          </div>
          <logout-icon size="24" />
        </template>
      </admin-navbar>
      <div class="m-4">
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>
