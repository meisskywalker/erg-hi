<template>
  <div
    class="bg-grey-50 min-w-[14rem] flex flex-col items-center rounded-2xl overflow-hidden h-screen max-h-[calc(100vh-1rem)] -ml-[14.5rem] lg:m-0"
  >
    <div class="h-12 flex items-center">
      <h1 class="text-2xl font-medium text-grey-900 py-2">ERG - HI</h1>
    </div>
    <div class="flex-1 w-full px-6 py-4 flex flex-col gap-4">
      <slot name="menus" />
    </div>
    <div
      class="h-10 w-full flex p-6 items-center bg-brand-600 text-grey-200 gap-2 cursor-pointer transition duration-200 hover:bg-brand-800"
    >
      <slot name="bottom-menu" />
    </div>
  </div>
</template>
