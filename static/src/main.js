/** @odoo-module **/

import { Product } from './components/Product';
import { mount } from '@odoo/owl';
document.addEventListener('DOMContentLoaded', async function () {
  mount(Product, { target: document.body });
});
